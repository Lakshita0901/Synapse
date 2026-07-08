from langchain_google_genai import ChatGoogleGenerativeAI


def get_llm():
    """
    Initialize and return the Gemini chat model.
    """

    llm = ChatGoogleGenerativeAI(
        model="gemini-2.5-flash",
        temperature=0,
    )

    return llm