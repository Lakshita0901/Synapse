from pathlib import Path

from app.loaders.document_loader import load_document
from app.splitters.text_splitter import split_documents
from app.cleaners.cleaners import clean_documents
from app.preprocessors.metadata_cleaner import clean_metadata
from app.vectorstores.chroma_store import store_documents
from dotenv import load_dotenv

load_dotenv()

def ingest_document(file_path: str):
    documents = load_document(file_path)

    cleaned_documents = clean_documents(documents)

    clean_metadata_documents = clean_metadata(cleaned_documents)

    chunks = split_documents(clean_metadata_documents)

    store_documents(chunks)

    return chunks

def main():

    file_path = input("Enter document path: ").strip()

    path = Path(file_path)

    if not path.exists():
        print(" File does not exist.")
        return

    try:
        chunks = ingest_document(str(path))

        print(f"Successfully created {len(chunks)} chunks.")

    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()