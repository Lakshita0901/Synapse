from langchain_community.document_loaders import WebBaseLoader


def load_url(url: str):
    """
    Load a webpage and return LangChain Documents.
    """

    loader = WebBaseLoader(url)

    return loader.load()