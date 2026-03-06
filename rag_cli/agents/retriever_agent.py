from retriever import retrieve

def retrieve_context(query):

    results = retrieve(query, top_k=5)

    chunks = [r[0] for r in results]

    return chunks, results