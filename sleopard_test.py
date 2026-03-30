from snowleopard import SnowLeopardClient
from dotenv import load_dotenv
import os

load_dotenv() 
api_key = os.getenv("API_KEY")
print(api_key)


client = SnowLeopardClient(api_key=api_key)
response = client.retrieve(
    datafile_id="20c7ab97fb534efaa9ec8c461135e0dc",
    user_query="Give me top 20 songs by Billie Eilish"
)
print(response.data[0].rows)
