from langchain_community.document_loaders import TextLoader


def load_txt(file_path: str):
    """
    Loads a TXT file and returns LangChain Documents.
    """

    loader = TextLoader(
        file_path=file_path,
        encoding="utf-8"
    )

    return loader.load()