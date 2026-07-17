from langchain_community.document_loaders import TextLoader

def load_markdown(file_path:str):
    """
    Loads Markdown file.
    """
    loader=TextLoader(
        file_path=file_path,encoding="utf-8"

    )
    return loader.load()