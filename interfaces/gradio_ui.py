import gradio as gr
from openai import OpenAI
from tools.tool_handler import handle_tool_calls, TOOLS



MODEL = "qwen2.5:3b"
client = OpenAI(base_url="http://localhost:11434/v1/", api_key="ollama")

def launch_chat(system_prompt, query_service):
    history = []

    def chat_fn(user_message, history):
        """
        Chat function for Gradio interface with tool-augmented OpenAI model.
        
        Args:
            user_message (str): The user's input message.
            history (list): List of previous messages, each a dict with 'role' and 'content'.
            query_service (TrainQueryService): Service to handle train queries.
            
        Returns:
            str: Assistant's response.
        """

        history = [{'role': h['role'], 'content': h['content']} for h in history]

        messages = (
            [{'role': 'system', 'content': system_prompt()}]
            + history
            + [{'role': 'user', 'content': user_message}]
        )

        response = client.chat.completions.create(
            model=MODEL,
            messages=messages,
            tools=TOOLS()
        )

        choice = response.choices[0]

        if choice.finish_reason == "tool_calls":
            assistant_message = choice.message

            messages.append({
                "role": "assistant",
                "content": assistant_message.content,
                "tool_calls": [
                    {
                        "id": tc.id,
                        "type": tc.type,
                        "function": {
                            "name": tc.function.name,
                            "arguments": tc.function.arguments
                        }
                    } for tc in assistant_message.tool_calls
                ]
            })

            tool_responses = handle_tool_calls(assistant_message, query_service)
            messages.extend(tool_responses)

            response = client.chat.completions.create(
                model=MODEL,
                messages=messages
            )


        return response.choices[0].message.content
    
    gr.ChatInterface(fn=chat_fn).launch()