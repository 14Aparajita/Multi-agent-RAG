from transformers import pipeline

reason_model = pipeline(
    "text-generation",
    model="TinyLlama/TinyLlama-1.1B-Chat-v1.0",
    max_new_tokens=200
)

def summarize_context(query, chunks):

    context = "\n\n".join(chunks)

    prompt = f"""
You are a research assistant.

Extract the most relevant information to answer the question.

Question:
{query}

Context:
{context}

Relevant information:
"""

    output = reason_model(prompt)

    text = output[0]["generated_text"]

    return text.split("Relevant information:")[-1].strip()