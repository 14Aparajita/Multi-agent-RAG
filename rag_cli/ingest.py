import os
import pickle
import faiss
import numpy as np

from sentence_transformers import SentenceTransformer
from pypdf import PdfReader


def ingest_documents(folder_path):

    print("Loading embedding model...")
    model = SentenceTransformer("all-MiniLM-L6-v2")

    chunks = []
    metadata_list = []

    for filename in os.listdir(folder_path):

        if filename.endswith(".pdf"):

            print("Processing:", filename)

            reader = PdfReader(os.path.join(folder_path, filename))

            for page_num, page in enumerate(reader.pages):

                text = page.extract_text()

                if text:

                    chunk_size = 800

                    for i in range(0, len(text), chunk_size):

                        chunk = text[i:i+chunk_size]

                        chunks.append(chunk)

                        metadata_list.append({
                            "source": filename,
                            "page": page_num + 1
                        })

    print("Creating embeddings...")

    embeddings = model.encode(chunks)

    embeddings = np.array(embeddings)

    faiss.normalize_L2(embeddings)

    dimension = embeddings.shape[1]

    index = faiss.IndexFlatIP(dimension)

    index.add(embeddings)

    os.makedirs("vectorstore", exist_ok=True)

    faiss.write_index(index, "vectorstore/index.faiss")

    with open("vectorstore/chunks.pkl", "wb") as f:
        pickle.dump(chunks, f)

    with open("vectorstore/metadata.pkl", "wb") as f:
        pickle.dump(metadata_list, f)

    print("Ingestion complete!")