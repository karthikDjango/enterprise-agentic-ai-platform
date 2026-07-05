import os

from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from tavily import TavilyClient

# Load environment variables
load_dotenv()

# ==========================
# Gemini Configuration
# ==========================

GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
RAG_RELEVANCE_THRESHOLD = 0.4

model = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    google_api_key=GOOGLE_API_KEY,
    temperature=0,
)

# ==========================
# Tavily Configuration
# ==========================

TAVILY_API_KEY = os.getenv("TAVILY_API_KEY")

tavily_client = TavilyClient(api_key=TAVILY_API_KEY)