from snowleopard import SnowLeopardClient
from dotenv import load_dotenv
import os

load_dotenv() 
api_key = os.getenv("API_KEY")
print(api_key)
datafile_id = os.getenv("DATAFILE_ID")


client = SnowLeopardClient(api_key=api_key)
response = client.retrieve(
    datafile_id=datafile_id,
    user_query="Give me top 20 songs by Billie Eilish"
)
print(response.data[0].rows)
