from agents.query_agent import rewrite_query
from agents.retriever_agent import retrieve_context
from agents.reasoning_agent import summarize_context
from agents.answer_agent import generate_final_answer
from agents.citation_agent import format_sources


def multi_agent_rag(query):

    improved_query = rewrite_query(query)

    chunks, results = retrieve_context(improved_query)

    summarized_context = summarize_context(query, chunks)

    answer = generate_final_answer(query, summarized_context)

    sources = format_sources(results)

    return answer, sources