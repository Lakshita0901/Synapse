from pathlib import Path

from .pdf_loader import load_pdf
from .docx_loader import load_docx
from .txt_loader import load_txt
from .markdown_loader import load_markdown
from .pptx_loader import load_pptx
from .image_loader import load_image
from .url_loader import load_url
from .youtube_loader import load_youtube


IMAGE_EXTENSIONS = {
    ".png",
    ".jpg",
    ".jpeg",
}


def is_youtube_url(url: str) -> bool:
    """
    Check whether the given URL is a YouTube link.
    """
    return (
        "youtube.com" in url
        or "youtu.be" in url
    )


def load_document(source: str):
    """
    Load a document from a local file or URL.

    Supported Sources:
        - PDF
        - DOCX
        - TXT
        - Markdown
        - PPTX
        - PNG/JPG/JPEG
        - Website URLs
        - YouTube URLs
    """

    # ---------------------------
    # URL Routing
    # ---------------------------
    if source.startswith(("http://", "https://")):
        if is_youtube_url(source):
            return load_youtube(source)

        return load_url(source)

    # ---------------------------
    # File Routing
    # ---------------------------
    extension = Path(source).suffix.lower()

    if extension == ".pdf":
        return load_pdf(source)

    elif extension == ".docx":
        return load_docx(source)

    elif extension == ".txt":
        return load_txt(source)

    elif extension == ".md":
        return load_markdown(source)

    elif extension == ".pptx":
        return load_pptx(source)

    elif extension in IMAGE_EXTENSIONS:
        return load_image(source)

    raise ValueError(
        f"Unsupported input type: '{extension}'. "
        "Supported types are: PDF, DOCX, TXT, Markdown, PPTX, PNG, JPG, JPEG, Website URLs, and YouTube URLs."
    )