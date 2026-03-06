from transformers import pipeline

rewrite_model = pipeline(
    "text-generation",
    model="TinyLlama/TinyLlama-1.1B-Chat-v1.0",
    max_new_tokens=60
)

def rewrite_query(query):

    prompt = f"""
Rewrite the user question to improve semantic search.

Question: {query}

Improved query:
"""

    output = rewrite_model(prompt)

    text = output[0]["generated_text"]

    return text.split("Improved query:")[-1].strip()