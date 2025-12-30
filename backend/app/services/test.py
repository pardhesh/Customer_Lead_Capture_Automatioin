from dotenv import load_dotenv
import os

#ignore this file. this is for only test
load_dotenv()  

groq_api_key = os.getenv("GROQ_API_KEY")

print(groq_api_key)  
