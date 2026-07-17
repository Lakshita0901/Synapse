from app.chains import get_rag_chain


def main():
    rag = get_rag_chain()

    while True:
        question = input("\nAsk a question (or 'exit'): ")

        if question.lower() == "exit":
            break

        result = rag(question)

        print("\nAnswer:\n")
        print(result["answer"])

        print("\nSources:\n")

        for retrieval_result in result["documents"]:
            doc = retrieval_result.document

            print(
                f"- {doc.metadata.get('source')} "
                f"(Page {doc.metadata.get('page_number')}) "
                f"(Distance: {retrieval_result.distance:.4f})"
            )



if __name__ == "__main__":
    main()