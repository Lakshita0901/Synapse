from app.retrievers import RetrievalResult


def select_diverse_chunks(
    results: list[RetrievalResult],
    k: int = 4,
):
    """
    Placeholder implementation.

    Returns the first k retrieval results.
    """

    return results[:k]

from difflib import SequenceMatcher


def text_similarity(text1: str, text2: str) -> float:
    """
    Returns similarity between two text strings.
    """

    return SequenceMatcher(
        None,
        text1,
        text2,
    ).ratio()

