from pathlib import Path


from app.splitters.text_splitter import split_documents
from app.cleaners.cleaners import clean_documents
from app.preprocessors.metadata_cleaner import clean_metadata
from app.vectorstores.chroma_store import store_documents
from dotenv import load_dotenv
from app.loaders.loader_factory import load_document
from app.preprocessors.document_metadata import enrich_document_metadata
load_dotenv()

def ingest_document(source: str):
    documents = load_document(source)

    documents = enrich_document_metadata(documents, source)

    documents = clean_documents(documents)

    documents = clean_metadata(documents)

    chunks = split_documents(documents)
    store_documents(chunks)

    return {
    "chunks": chunks,
    "num_chunks": len(chunks),
    "source":source,
}



