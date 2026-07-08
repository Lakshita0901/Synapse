from langchain_core.prompts import ChatPromptTemplate


def get_rag_prompt():
    """
    Returns the prompt template used for RAG.
    """

    prompt = ChatPromptTemplate.from_template(
        """
You are Synapse, an AI-powered Second Brain.

Answer the user's question ONLY using the provided context.

If the answer cannot be found in the context, reply:

"I don't have enough information in the provided documents."

Do not make up information.
Do not use outside knowledge.

Context:
{context}

Question:
{question}

Answer:
"""
    )

    return prompt