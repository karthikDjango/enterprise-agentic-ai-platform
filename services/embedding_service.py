from langchain_google_genai import GoogleGenerativeAIEmbeddings

from config import GOOGLE_API_KEY


_embeddings = GoogleGenerativeAIEmbeddings(
    model="models/gemini-embedding-001",
    google_api_key=GOOGLE_API_KEY,
)



def get_embeddings():
    """
    Return the Gemini embedding model.
    """
    return _embeddings