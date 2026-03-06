from transformers import pipeline

answer_model = pipeline(
    "text-generation",
    model="TinyLlama/TinyLlama-1.1B-Chat-v1.0",
    max_new_tokens=200
)

def generate_final_answer(query, summarized_context):

    prompt = f"""
Use the information below to answer the question.

Information:
{summarized_context}

Question:
{query}

Answer:
"""

    output = answer_model(prompt)

    text = output[0]["generated_text"]

    return text.split("Answer:")[-1].strip()