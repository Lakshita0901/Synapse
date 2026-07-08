from pathlib import Path

from langchain_community.document_loaders import (
    UnstructuredPDFLoader,
)


def load_document(file_path: str):

    extension = Path(file_path).suffix.lower()

    if extension == ".pdf":
        loader = UnstructuredPDFLoader(
            file_path=file_path,
            mode="elements",
        )

    else:
        raise ValueError(
            f"Unsupported file type: {extension}"
        )

    return loader.load()