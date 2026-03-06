from transformers import pipeline

generator = None


def load_model():

    global generator

    if generator is None:

        print("Loading LLM... (first time may take 1-2 minutes)")

        generator = pipeline(
            "text-generation",
            model="TinyLlama/TinyLlama-1.1B-Chat-v1.0",
            max_new_tokens=200
        )


def generate_answer(question, context_chunks):

    load_model()

    context = "\n\n".join(context_chunks)

    prompt = f"""
Use the context below to answer the question.

Context:
{context}

Question:
{question}

Answer:
"""

    output = generator(prompt)

    return output[0]["generated_text"].split("Answer:")[-1].strip()