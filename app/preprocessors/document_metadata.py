from langchain_core.documents import Document

from pathlib import Path
from datetime import datetime
import uuid
from urllib.parse import urlparse


def enrich_document_metadata(
    documents: list[Document],
    source: str,
) -> list[Document]:
    """
    Add Synapse-specific metadata to every document.

    Args:
        documents: Documents returned by a loader.
        source: Original source (file path or URL).

    Returns:
        Documents with enriched metadata.
    """

    # Generate one unique ID for the entire document
    document_id = str(uuid.uuid4())

    # Timestamp
    ingested_at = datetime.now().isoformat()

    # Extract filename and file type
    parsed = urlparse(source)

    if parsed.scheme in ("http", "https"):
        # URL or YouTube
        filename = parsed.netloc + parsed.path

        if "youtube.com" in parsed.netloc or "youtu.be" in parsed.netloc:
            file_type = "youtube"
        else:
            file_type = "url"

    else:
        path = Path(source)
        filename = path.name
        file_type = path.suffix.lower().lstrip(".")

    # Attach metadata to every document
    for doc in documents:
        doc.metadata.update(
            {
                "document_id": document_id,
                "filename": filename,
                "file_type": file_type,
                "source": source,
                "ingested_at": ingested_at,
                "chunk_source": source,
            }
        )

    return documents