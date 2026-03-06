def format_sources(results):

    sources = []

    for chunk, score, meta in results:

        sources.append({
            "document": meta["source"],
            "page": meta["page"],
            "score": float(score)
        })

    return sources