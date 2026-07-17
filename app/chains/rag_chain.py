from app.retrievers import  SynapseRetriever
from app.llms import get_llm
from app.prompts import get_rag_prompt
MAX_DISTANCE = 0.8

def get_rag_chain():
    """
    Creates and returns a simple RAG pipeline.
    """

    retriever =SynapseRetriever()
    llm = get_llm()
    prompt = get_rag_prompt()

    def ask(question: str):
        # Retrieve relevant documents
        results = retriever.retrieve_with_scores(question)
        

        relevant_results = [
            result
            for result in results
            if result.distance <= MAX_DISTANCE
]
        
        
        from app.postprocessing import select_diverse_chunks

        relevant_results = select_diverse_chunks(
            relevant_results,
            k=4,
        )
        if not relevant_results:
            return {
                "answer": "I couldn't find sufficiently relevant information in the provided documents.",
                "documents": [],
            }
        # Combine retrieved chunks into one context string
        context = "\n\n".join(
    result.document.page_content
    for result in relevant_results
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
        "documents":relevant_results,
    }

    return ask