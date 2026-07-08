from langchain_chroma import Chroma

from app.embeddings.embedding_model import get_embedding_model


def store_documents(chunks):

    embeddings = get_embedding_model()

    vector_store = Chroma.from_documents(
        documents=chunks,
        embedding=embeddings,
        persist_directory="db"
    )

    return vector_store