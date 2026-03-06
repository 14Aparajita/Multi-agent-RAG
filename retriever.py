import faiss
import pickle
import numpy as np
from sentence_transformers import SentenceTransformer


model = SentenceTransformer("all-MiniLM-L6-v2")


def retrieve(query, top_k=3):

    index = faiss.read_index("vectorstore/index.faiss")

    with open("vectorstore/chunks.pkl", "rb") as f:
        chunks = pickle.load(f)

    with open("vectorstore/metadata.pkl", "rb") as f:
        metadata_list = pickle.load(f)

    query_vector = model.encode([query])

    query_vector = np.array(query_vector)

    faiss.normalize_L2(query_vector)

    D, I = index.search(query_vector, top_k)

    results = []

    for idx, dist in zip(I[0], D[0]):

        results.append(
            (
                chunks[idx],
                dist,
                metadata_list[idx]
            )
        )

    return results