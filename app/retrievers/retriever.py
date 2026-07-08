from langchain_chroma import Chroma

from app.embeddings.embedding_model import get_embedding_model


DB_DIRECTORY = "db"


def get_retriever(k: int = 4):
    """
    Load the persisted Chroma vector store and return a retriever.

    Args:
        k (int): Number of most relevant chunks to retrieve.

    Returns:
        BaseRetriever: LangChain retriever instance.
    """

    embedding_model = get_embedding_model()

    vector_store = Chroma(
        persist_directory=DB_DIRECTORY,
        embedding_function=embedding_model,
    )

    retriever = vector_store.as_retriever(
        search_type="similarity",
        search_kwargs={"k": k},
    )

    return retriever