from langchain_google_genai import ChatGoogleGenerativeAI
import google.generativeai as genai


def get_llm():
    """
    Returns the LangChain chat model.
    """

    return ChatGoogleGenerativeAI(
        model="gemini-2.5-flash",
        temperature=0,
    )


def get_vision_model():
    """
    Returns the Gemini Vision model.
    """

    return genai.GenerativeModel("gemini-2.5-flash")