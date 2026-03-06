import argparse
from ingest import ingest_documents
from retriever import retrieve
from generator import generate_answer


def main():

    parser = argparse.ArgumentParser()

    parser.add_argument("--ingest", type=str, help="Folder path to ingest")

    args = parser.parse_args()

    if args.ingest:
        ingest_documents(args.ingest)
        return

    print("\nRAG Chat System Ready")
    print("Type 'exit' to quit\n")

    while True:

        query = input("Ask question: ")

        if query.lower() == "exit":
            break

        results = retrieve(query)

        context_chunks = [r[0] for r in results]

        answer = generate_answer(query, context_chunks)

        print("\n===== ANSWER =====\n")
        print(answer)

        print("\n===== SOURCES =====\n")

        for chunk, score, metadata in results:
            print(f"Score: {score:.4f}")
            print(f"Source: {metadata['source']} | Page: {metadata['page']}")
            print(chunk[:200])
            print("-----")


if __name__ == "__main__":
    main()