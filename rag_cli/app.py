import streamlit as st
import os

from ingest import ingest_documents
from agents.orchestrator import multi_agent_rag


# -----------------------------
# PAGE CONFIG
# -----------------------------
st.set_page_config(
    page_title="Multi-Agent RAG Chat Assistant",
    page_icon="🤖",
    layout="wide"
)

st.title("🤖 Multi-Agent RAG Document Chat Assistant")


# -----------------------------
# SIDEBAR SETTINGS
# -----------------------------
st.sidebar.header("Settings")

st.sidebar.markdown(
"""
System Architecture:

User Query  
→ Query Agent  
→ Retriever Agent  
→ Reasoning Agent  
→ Answer Agent  
→ Citation Agent
"""
)


# -----------------------------
# DOCUMENT UPLOAD
# -----------------------------
st.sidebar.subheader("Upload Documents")

uploaded_file = st.sidebar.file_uploader(
    "Upload PDF",
    type=["pdf"]
)

if uploaded_file:

    os.makedirs("data", exist_ok=True)

    save_path = os.path.join("data", uploaded_file.name)

    with open(save_path, "wb") as f:
        f.write(uploaded_file.getbuffer())

    if st.sidebar.button("Run Ingestion"):

        with st.spinner("Processing document..."):
            ingest_documents("data")

        st.sidebar.success("Document indexed successfully!")


# -----------------------------
# CHAT MEMORY
# -----------------------------
if "messages" not in st.session_state:
    st.session_state.messages = []


# -----------------------------
# DISPLAY CHAT HISTORY
# -----------------------------
for message in st.session_state.messages:

    with st.chat_message(message["role"]):
        st.markdown(message["content"])

        if "sources" in message:

            st.markdown("#### 📄 Sources")

            for src in message["sources"]:

                st.write(
                    f"{src['document']} | Page {src['page']} | Score {src['score']:.3f}"
                )


# -----------------------------
# USER INPUT
# -----------------------------
query = st.chat_input("Ask a question about your documents...")

if query:

    # Show user message
    with st.chat_message("user"):
        st.markdown(query)

    st.session_state.messages.append(
        {"role": "user", "content": query}
    )


    # Run multi-agent RAG pipeline
    with st.spinner("Agents are reasoning..."):
        answer, sources = multi_agent_rag(query)


    # Show assistant message
    with st.chat_message("assistant"):

        message_placeholder = st.empty()

        full_text = ""

        # typing animation
        for char in answer:
            full_text += char
            message_placeholder.markdown(full_text)

        st.markdown("#### 📄 Sources")

        for src in sources:

            st.write(
                f"{src['document']} | Page {src['page']} | Score {src['score']:.3f}"
            )


    # Save assistant message
    st.session_state.messages.append(
        {
            "role": "assistant",
            "content": answer,
            "sources": sources
        }
    )
