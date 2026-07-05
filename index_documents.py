from services.document_service import load_documents
from services.vector_store_service import create_vector_store


def main():
    documents = load_documents()

    if not documents:
        print("No documents found.")
        return

    create_vector_store(documents)

    print(f"Indexed {len(documents)} document(s).")


if __name__ == "__main__":
    main()