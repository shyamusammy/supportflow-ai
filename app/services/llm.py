import os
from dotenv import load_dotenv
from crewai import LLM

load_dotenv()

llm = LLM(
    model="gemini/gemini-0.5-flash",
    api_key=os.getenv("GOOGLE_API_KEY"),
    temperature=0.2,
)