from app.retrievers import get_retriever
from app.llms import get_llm
from app.prompts import get_rag_prompt


def get_rag_chain():
    """
    Creates and returns a simple RAG pipeline.
    """

    retriever = get_retriever()
    llm = get_llm()
    prompt = get_rag_prompt()

    def ask(question: str):
        # Retrieve relevant documents
        documents = retriever.invoke(question)

        # Combine retrieved chunks into one context string
        context = "\n\n".join(
            doc.page_content for doc in documents
        )

        # Fill the prompt template
        formatted_prompt = prompt.invoke(
            {
                "context": context,
                "question": question,
            }
        )

        # Generate answer
        response = llm.invoke(formatted_prompt)

        return {
            "answer": response.content,
            "documents": documents,
        }

    return ask