import os
import subprocess
import sys
from dotenv import load_dotenv

from pydantic_ai import Agent, RunContext
from snowleopard import SnowLeopardClient

from text2speech import main as run_speech_capture, spoken_texts as spoken_text

load_dotenv() 

# Get model from environment variable with default
# PydanticAI model format: 'provider:model-name' (e.g., 'anthropic:claude-sonnet-4-5', 'openai:gpt-4o')
MODEL_NAME = os.environ.get('MODEL_NAME', 'anthropic:claude-sonnet-4-5')

# Create a pydantic agent.
# Note! This requires the appropriate API key env var for the model provider
agent = Agent(
    MODEL_NAME,
    instructions='Be concise, reply with one sentence.',
)

# Instantiate your Snow Leopard Client.
# Note! This requires env var SNOWLEOPARD_API_KEY
snowy = SnowLeopardClient(api_key= os.environ.get('SNOWLEOPARD_API_KEY'))

# This is a datafile id that corresponds to a superheroes.db datafile uploaded at http//try.snowleopard.ai
datafile_id = os.environ.get('SNOWLEOPARD_DATAFILE_ID')
if not datafile_id:
    print("environment variable SNOWLEOPARD_DATAFILE_ID required", file=sys.stderr)
    sys.exit(1)

# Define the get_data tool for your agent. This allows the agent to retrieve data using Snow Leopard
# The docstring becomes the tool description, so this is part of the agent context.
@agent.tool
def get_data(ctx: RunContext[str], user_query: str) -> str:
    print(f"[Tool Call]: get_data {user_query}")
    response = snowy.retrieve(user_query=user_query, datafile_id="20c7ab97fb534efaa9ec8c461135e0dc")
    print(f"[Tool Response]: {response}")
    return str(response)

def ask_clai(question: str):    
    command = ["uv", "run", "clai", "--agent", "agent:agent"]
    
    try:
        # Use input to automate the question
        subprocess.run(command, input=f"{question}\n", text=True)
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    run_speech_capture()
    ask_clai(" ".join(spoken_text))