import json

def handle_tool_calls(message, query_service):
    responses = []
    print(message)
    for tool_call in message.tool_calls:
        name = tool_call.function.name
        arguments = json.loads(tool_call.function.arguments)

        if name == "find_trains":
            origin = arguments.get("origin")
            destination = arguments.get("destination")

            output = query_service.get_trains_between(origin, destination)
            if not isinstance(output, str):
                output = json.dumps(output)

        elif name == "train_schedule":
            train_number = arguments.get("train_number")
            origin = arguments.get("origin")

            output = query_service.get_train_schedule(train_number, origin)
            if not isinstance(output, str):
                output = json.dumps(output)

        elif name == "check_running_days":
            train_number = arguments.get("train_number")

            output = query_service.get_running_days(train_number)
            if not isinstance(output, str):
                output = json.dumps(output)

        elif name == "train_routes":
            train_number = arguments.get("train_number")

            output = query_service.get_train_routes(train_number)
            if not isinstance(output, str):
                output = json.dumps(output)

        else:
            output = f"Unknown tool: {name}"

        responses.append({
            "role": "tool",
            "tool_call_id": tool_call.id,
            "content": output
        })

    return responses

def TOOLS():
    return [
        {
            "type": "function",
            "function": {
                "name": "find_trains",
                "description": "Find trains between two stations",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "origin": {
                            "type": "string",
                            "description": "Origin station name"
                        },
                        "destination": {
                            "type": "string",
                            "description": "Destination station name"
                        }
                    },
                    "required": ["origin", "destination"]
                }
            }
        },
        {
            "type": "function",
            "function": {
                "name": "train_schedule",
                "description": "Get departure and arrival schedule of a train",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "train_number": {
                            "type": "string",
                            "description": "Train number"
                        },
                        "origin": {
                            "type": "string",
                            "description": "Optional station name"
                        }
                    },
                    "required": ["train_number"]
                }
            }
        },
        {
            "type": "function",
            "function": {
                "name": "check_running_days",
                "description": "Check which days a train runs",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "train_number": {
                            "type": "string",
                            "description": "Train number"
                        }
                    },
                    "required": ["train_number"]
                }
            }
        },
        {
            "type": "function",
            "function": {
                "name": "train_routes",
                "description": "List all stations in a train route",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "train_number": {
                            "type": "string",
                            "description": "Train number"
                        }
                    },
                    "required": ["train_number"]
                }
            }
        }
    ]