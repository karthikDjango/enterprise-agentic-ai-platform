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
GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")
GITHUB_OWNER = os.getenv("GITHUB_OWNER")
GITHUB_REPOSITORY = os.getenv("GITHUB_REPOSITORY")
# ==========================
# Jira Configuration
# ==========================

JIRA_BASE_URL = os.getenv("JIRA_BASE_URL")
JIRA_EMAIL = os.getenv("JIRA_EMAIL")
JIRA_API_TOKEN = os.getenv("JIRA_API_TOKEN")

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