from pathlib import Path

from langchain_community.document_loaders import (
    PyPDFLoader,
    TextLoader,
)


SUPPORTED_EXTENSIONS = {
    ".pdf": PyPDFLoader,
    ".txt": TextLoader,
}


def load_documents(folder_path: str = "documents"):
    """
    Load all supported documents from the documents folder.
    """

    documents = []

    folder = Path(folder_path)

    if not folder.exists():
        return documents

    for file in folder.iterdir():

        if not file.is_file():
            continue

        loader_class = SUPPORTED_EXTENSIONS.get(file.suffix.lower())

        if loader_class is None:
            continue

        loader = loader_class(str(file))

        documents.extend(loader.load())

    return documents