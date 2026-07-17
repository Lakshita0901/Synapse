from langchain_chroma import Chroma

from app.embeddings import get_embedding_model
from .models import RetrievalResult

DB_DIRECTORY = "db"


class SynapseRetriever:
    """
    Handles all retrieval operations for Synapse.
    """

    def __init__(self):
        self.embedding_model = get_embedding_model()

        self.vector_store = Chroma(
            persist_directory=DB_DIRECTORY,
            embedding_function=self.embedding_model,
        )

    def retrieve(self, query: str, k: int = 4):
        """
        Perform semantic similarity search.

        Returns:
            List[Document]
        """

        return self.vector_store.similarity_search(
            query=query,
            k=k,
        )

    def retrieve_with_scores(self, query: str, k: int = 4):

        results = self.vector_store.similarity_search_with_score(
            query=query,
            k=k,
    )

        retrieval_results = []

        for document, distance in results:

            retrieval_results.append(
                    RetrievalResult(
                        document=document,
                        distance=distance,
                    )
                )
        return retrieval_results   

    def retrieve_similarity(
    self,
    query: str,
    k: int = 4,
    ):
        results = self.vector_store.similarity_search_with_score(
        query=query,
        k=k,
    )

        return [
            RetrievalResult(
                document=document,
                distance=distance,
            )
            for document, distance in results
        ]


def retrieve_mmr(
    self,
    query: str,
    k: int = 4,
    fetch_k: int = 20,
    lambda_mult: float = 0.5,
):
    return self.vector_store.max_marginal_relevance_search(
        query=query,
        k=k,
        fetch_k=fetch_k,
        lambda_mult=lambda_mult,
    )