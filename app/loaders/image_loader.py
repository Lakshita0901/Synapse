from PIL import Image
from langchain_core.documents import Document

from app.llms.gemini import get_vision_model
from app.prompts.image_prompt import IMAGE_EXTRACTION_PROMPT

from pathlib import Path

def load_image(image_path: str):
    """
    Load an image using Gemini Vision and return LangChain Documents.
    """

    model = get_vision_model()

    image = Image.open(image_path)

    response = model.generate_content(
        [
            IMAGE_EXTRACTION_PROMPT,
            image,
        ]
    )

    return [
        Document(
            page_content=response.text,
            metadata={
                "source": image_path,
                "filename": Path(image_path).name,
                "file_type": "image",
            },
        )
    ]