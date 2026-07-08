# Synapse

Synapse is a modular Retrieval-Augmented Generation (RAG) system that allows users to chat with their personal knowledge base.

The project is built from scratch using LangChain, Gemini, and ChromaDB with a clean, modular architecture designed for learning and production-ready extensibility.
## Features

- PDF ingestion pipeline
- Automatic document cleaning
- Metadata preprocessing
- Recursive chunking
- Gemini Embeddings
- Chroma Vector Database
- Semantic Retrieval
- Modular RAG Pipeline
- Source citations
- Gemini-powered question answering

## Architecture

```text
PDF
 │
 ▼
Document Loader
 │
 ▼
Document Cleaner
 │
 ▼
Metadata Cleaner
 │
 ▼
Text Splitter
 │
 ▼
Gemini Embeddings
 │
 ▼
ChromaDB

Question
 │
 ▼
Retriever
 │
 ▼
Relevant Chunks
 │
 ▼
Prompt Builder
 │
 ▼
Gemini
 │
 ▼
Answer + Sources
```
## Project structure
```text
app/
├── chains/
├── cleaners/
├── embeddings/
├── llms/
├── loaders/
├── preprocessors/
├── prompts/
├── retrievers/
├── splitters/
└── vectorstores/

chat.py
ingest.py
```

## Tech Stack

- Python
- LangChain
- Google Gemini
- ChromaDB
- Unstructured
- python-dotenv

## Roadmap

- [x] Modular RAG pipeline
- [x] Semantic retrieval
- [x] Source citations
- [ ] Retrieval scoring
- [ ] MMR Retrieval
- [ ] Metadata filtering
- [ ] Hybrid Search
- [ ] Reranking
- [ ] Conversation Memory
- [ ] Multi-document Workspaces