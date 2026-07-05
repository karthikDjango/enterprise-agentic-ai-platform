from services.vector_store_service import similarity_search
from services.prompt_service import get_system_prompt
from services.llm_service import ask_gemini_prompt


def rag_search(question: str) -> str:
    """
    Retrieve relevant documents and generate an answer.
    """

    documents = similarity_search(question)

    context = "\n\n".join(
        doc.page_content
        for doc in documents
    )

    prompt = f"""
{get_system_prompt()}

Answer the user's question using ONLY the context below.

If the answer is not present in the context,
say you don't know.

====================
Context
====================

{context}

====================
Question
====================

{question}
"""

    return ask_gemini_prompt(prompt)