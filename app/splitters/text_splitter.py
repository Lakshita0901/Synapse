# we will be using recursivecharactertextsplitter
# parametrs chunk size, overlap  defaults for pdf chunk_size=100 and chunk_overlap=200
from langchain_text_splitters import RecursiveCharacterTextSplitter

def split_documents(documents):

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=200,
    )

    chunks = splitter.split_documents(documents)

    return chunks
