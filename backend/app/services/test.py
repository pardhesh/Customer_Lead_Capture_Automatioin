from dotenv import load_dotenv
import os

load_dotenv()  # loads .env

groq_api_key = os.getenv("GROQ_API_KEY")

print(groq_api_key)  # test once
