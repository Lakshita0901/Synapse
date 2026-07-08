
from langchain_core.documents import Document


REMOVE_CATEGORIES = {
    "Footer",
    "Header",
}


def clean_documents(documents: list[Document]) -> list[Document]:
    """
    Remove unwanted document elements before chunking.
    """

    cleaned_documents = []

    for doc in documents:

        category = doc.metadata.get("category", "")

        text = doc.page_content.strip()

        # Remove headers and footers
        if category in REMOVE_CATEGORIES:
            continue

        # Remove empty elements
        if not text:
            continue

        cleaned_documents.append(doc)

    return cleaned_documents