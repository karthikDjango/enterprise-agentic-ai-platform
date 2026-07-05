from langchain_chroma import Chroma
from langchain_text_splitters import RecursiveCharacterTextSplitter

from services.embedding_service import get_embeddings
from config import RAG_RELEVANCE_THRESHOLD


DB_PATH = "vector_db"


text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=1000,
    chunk_overlap=200,
)


def create_vector_store(documents):
    """
    Create a Chroma vector store from documents.
    """

    chunks = text_splitter.split_documents(documents)

    vector_store = Chroma.from_documents(
        documents=chunks,
        embedding=get_embeddings(),
        persist_directory=DB_PATH,
    )

    return vector_store


def load_vector_store():
    """
    Load an existing Chroma vector store.
    """

    return Chroma(
        persist_directory=DB_PATH,
        embedding_function=get_embeddings(),
    )


def similarity_search(query, k=4):
    """
    Search the vector database.
    """

    vector_store = load_vector_store()

    return vector_store.similarity_search(query, k=k)

def has_relevant_documents(query: str) -> bool:
    """
    Check whether the vector store contains relevant documents.

    Returns:
        True  -> Relevant documents found
        False -> No relevant documents
    """

    vector_store = load_vector_store()

    results = vector_store.similarity_search_with_relevance_scores(
        query,
        k=1,
    )

    if not results:
        return False

    _, score = results[0]

    print(f"RAG Relevance Score: {score:.10f}")

    return score >= RAG_RELEVANCE_THRESHOLD