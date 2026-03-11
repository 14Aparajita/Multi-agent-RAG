# Multi-Agent RAG Document Chat Assistant

A **Multi-Agent Retrieval-Augmented Generation (RAG) system** that allows users to chat with PDF documents using a modular AI pipeline.

The system retrieves relevant document chunks from a FAISS vector database and uses a language model to generate grounded answers with citations.

This project demonstrates **modern AI system architecture combining vector search, multi-agent reasoning, and an interactive chat interface.**

---

# Project Architecture

The system follows a **multi-agent RAG pipeline**:

User Query
↓
Query Agent – improves search query
↓
Retriever Agent – semantic search using FAISS
↓
Reasoning Agent – extracts relevant information
↓
Answer Agent – generates final response
↓
Citation Agent – formats document sources
↓
Chat Interface using Streamlit

---

# Repository Structure

```id="i3xwpa"
Multi-agent-RAG/
│
└── rag_cli/
    │
    ├── agents/
    │   ├── query_agent.py
    │   ├── retriever_agent.py
    │   ├── reasoning_agent.py
    │   ├── answer_agent.py
    │   ├── citation_agent.py
    │   └── orchestrator.py
    │
    ├── app.py
    ├── ingest.py
    ├── retriever.py
    ├── generator.py
    ├── main.py
    │
    ├── data/
    ├── vectorstore/
    │
    └── requirements.txt
```

---

# Features

* Multi-agent RAG architecture
* Semantic search using FAISS
* PDF document ingestion
* Context-aware LLM answers
* Source citation with page numbers
* ChatGPT-style chat interface
* Document upload support
* Modular AI pipeline

---

# Technologies Used

* Python
* FAISS Vector Database
* Sentence Transformers
* HuggingFace Transformers
* TinyLlama LLM
* Streamlit Chat Interface

---

# Installation (Local Setup)

Clone the repository

```id="8ctuk8"
git clone https://github.com/YOUR_USERNAME/Multi-agent-RAG.git
cd Multi-agent-RAG/rag_cli
```

Create virtual environment

```id="l8rshg"
python -m venv venv
```

Activate environment

Windows

```id="m5q7m0"
venv\Scripts\activate
```

Mac / Linux

```id="y9vj3d"
source venv/bin/activate
```

Install dependencies

```id="p4fyri"
pip install -r requirements.txt
```

---

# Ingest Documents

Place PDF files inside the `data` folder.

Run ingestion pipeline:

```id="pb6c0e"
python main.py --ingest data
```

This will:

* extract text from PDFs
* split documents into chunks
* generate embeddings
* store vectors in FAISS index

The index will be saved in:

```id="c82ptf"
vectorstore/
```

---

# Run the Chat Application

Launch the Streamlit interface:

```id="i9coqg"
streamlit run app.py
```

Open the application in your browser:

```id="4pff0u"
http://localhost:8501
```

You can now chat with your documents.

---

# Example Queries

* What is blood pressure estimation?
* Summarize the ensemble AI approach described in the paper.
* What dataset was used for training?
* What are the limitations of the proposed method?

---

# Deploying on Streamlit Cloud

This project can be deployed using **Streamlit Community Cloud**.

---

# Step 1 — Push Code to GitHub

Ensure your repository structure is:

```id="0hhtf4"
Multi-agent-RAG/
│
└── rag_cli/
    ├── app.py
    ├── ingest.py
    ├── retriever.py
    ├── generator.py
    ├── main.py
    ├── agents/
    └── requirements.txt
```

Commit and push your code.

---

# Step 2 — Open Streamlit Cloud

Go to:

https://share.streamlit.io

Login using your GitHub account.

---

# Step 3 — Create New App

Click **New App**.

Fill the fields:

Repository

```id="vpb4to"
YOUR_USERNAME/Multi-agent-RAG
```

Branch

```id="hsm69m"
main
```

Main file path

```id="m7m8g2"
rag_cli/app.py
```

This is important because your app file is inside the **rag_cli folder**.

---

# Step 4 — Deploy

Click **Deploy**.

Streamlit will:

* clone the repository
* install dependencies from `requirements.txt`
* start the application

Deployment usually takes **2–5 minutes**.

---

# Step 5 — Access Your App

After deployment you will receive a public link:

```id="js3p7o"
https://your-app-name.streamlit.app
```

Anyone can access the application using this URL.

---

# Updating the App

Whenever you push updates to GitHub:

```id="kjw7zv"
git add .
git commit -m "update"
git push
```

Streamlit automatically redeploys the application.

---

# Future Improvements

* Hybrid search (BM25 + embeddings)
* RAG evaluation metrics
* Streaming token responses
* Knowledge graph integration
* Multi-document ranking
* GPU inference support

---

# License

MIT License

---

# Author

Developed as an AI engineering project demonstrating advanced RAG architecture and multi-agent reasoning systems.
