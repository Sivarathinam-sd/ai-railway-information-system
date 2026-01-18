from loaders.schedule_loader import ScheduleLoader
from repositories.train_repository import TrainRepository
from services.train_query_service import TrainQueryService
from interfaces.gradio_ui import launch_chat
from prompts.system_prompt import systemPrompt
from openai import OpenAI

# OpenAI client setup
MODEL = "qwen2.5:3b"
client = OpenAI(base_url="http://localhost:11434/v1/", api_key="ollama")

# Load schedules
loader = ScheduleLoader("data/EXP-TRAINS.json")
schedules = loader.load()

# Initialize repository & service
train_repo = TrainRepository(schedules)
query_service = TrainQueryService(train_repo.get_trains(), train_repo.get_stations())

launch_chat(systemPrompt, query_service)