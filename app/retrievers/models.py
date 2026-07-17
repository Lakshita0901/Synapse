from dataclasses import dataclass
from langchain_core.documents import Document


@dataclass
class RetrievalResult:
    """
    Represents a retrieved document and its distance
    from the user's query.
    """

    document: Document
    distance: float