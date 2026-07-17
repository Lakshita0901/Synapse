from pathlib import Path

from langchain_community.document_loaders import UnstructuredPDFLoader


def load_pdf(file_path: str):
    loader = UnstructuredPDFLoader(
        file_path=file_path,
        mode="elements",
    )

    return loader.load()