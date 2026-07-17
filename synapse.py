from pathlib import Path

from app.services import ingest_document


def main():
    while True:
        print("\n" + "=" * 40)
        print("          SYNAPSE")
        print("   Your Personal AI Knowledge Base")
        print("=" * 40)

        print("1. Add Knowledge")
        print("2. Chat")
        print("3. View Knowledge Base")
        print("4. Delete Knowledge")
        print("5. Exit")

        choice = input("\nEnter your choice: ").strip()

        if choice == "1":

            source = input("\nEnter file path or URL: ").strip()

            # Validate only local files
            if not source.startswith(("http://", "https://")):
                path = Path(source)

                if not path.exists():
                    print("\nFile not found!")
                    continue

                source = str(path)

            try:
                result = ingest_document(source)

                print("\nKnowledge added successfully!")
                print(f"Source: {result['source']}")
                print(f"Chunks stored: {result['num_chunks']}")

            except Exception as e:
                print(f"\nError: {e}")

        elif choice == "2":
            print("\nChat coming soon...")

        elif choice == "3":
            print("\nView Knowledge Base coming soon...")

        elif choice == "4":
            print("\nDelete Knowledge coming soon...")

        elif choice == "5":
            print("\nGoodbye!")
            break

        else:
            print("\nInvalid choice! Please try again.")


if __name__ == "__main__":
    main()