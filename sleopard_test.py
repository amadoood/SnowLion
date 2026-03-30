from snowleopard import SnowLeopardClient
from dotenv import load_dotenv
import os

load_dotenv() 
api_key = os.getenv("API_KEY")
print(api_key)


client = SnowLeopardClient(api_key=api_key)
response = client.retrieve(
    datafile_id="superheroes",
    user_query="Give me a list of the first 100 superheroes."
)
print(response.data[0].rows)
