def clean_metadata(documents):
    ALLOWED_METADATA = [
        "source",
        "page_number",
        "category",
    ]

    for doc in documents:
        doc.metadata = {
            key: doc.metadata.get(key)
            for key in ALLOWED_METADATA
        }

    return documents