from langchain_community.document_loaders import UnstructuredPowerPointLoader


def load_pptx(file_path: str):
    """
    Loads a PowerPoint presentation and returns LangChain Documents.
    """

    loader = UnstructuredPowerPointLoader(
        file_path=file_path,
        mode="elements",
    )

    return loader.load()