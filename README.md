# Synapse



Synapse is a modular Retrieval-Augmented Generation (RAG) system that enables users to build and chat with a personal knowledge base from multiple data sources.

Built from scratch using LangChain, Google Gemini, and ChromaDB, Synapse focuses on clean architecture, modular design, and extensibility while demonstrating the core components of modern RAG systems.
## Why Synapse?

Large Language Models cannot answer questions about your personal documents by default.

Synapse bridges this gap by ingesting data from multiple sources, converting it into vector embeddings, retrieving the most relevant context, and grounding Gemini's responses in your own knowledge base.

## Features

### Universal Document Ingestion

- PDF
- DOCX
- TXT
- Markdown
- PowerPoint (PPTX)
- Images (Gemini Vision)
- Website URLs
- YouTube videos

### Knowledge Processing

- Automatic document cleaning
- Metadata preprocessing
- Universal loader factory
- Recursive text chunking
- Gemini Embeddings
- Chroma Vector Database

### Retrieval Pipeline

- Semantic Retrieval
- Similarity Score Filtering
- Source Citations
- Modular RAG Pipeline
- Gemini-powered Question Answering

### Architecture

- Service Layer
- Factory Pattern
- Modular Project Structure
## Architecture

```text
                 User Source
                      │
      ┌───────────────┼────────────────┐
      │               │                │
    Files          Website          YouTube
(PDF/DOCX/TXT/       URL              URL
 MD/PPTX/Image)
      │
      ▼
 Universal Loader Factory
      │
      ▼
 LangChain Documents
      │
      ▼
 Document Cleaner
      │
      ▼
 Metadata Enrichment
      │
      ▼
 Metadata Cleaner
      │
      ▼
 Recursive Text Splitter
      │
      ▼
 Gemini Embeddings
      │
      ▼
 ChromaDB
      │
      ▼
 Semantic Retriever
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
## Project Structure

```text
app/
├── chains/
├── cleaners/
├── embeddings/
├── knowledge/
├── llms/
├── loaders/
├── postprocessing/
├── preprocessors/
├── prompts/
├── retrievers/
├── services/
├── splitters/
└── vectorstores/

synapse.py
```

## Tech Stack

- Python
- LangChain
- Google Gemini
- ChromaDB
- Unstructured
- Pillow
- BeautifulSoup
- python-dotenv

## Roadmap

### Completed

- [x] Universal multi-source ingestion
- [x] Modular RAG pipeline
- [x] Semantic retrieval
- [x] Similarity score filtering
- [x] Source citations
- [x] Gemini Vision support
- [x] Universal loader factory

### In Progress

- [ ] SQLite document catalog
- [ ] Knowledge management
- [ ] Metadata filtering

### Planned

- [ ] Improved MMR retrieval
- [ ] Hybrid Search
- [ ] Reranking
- [ ] Conversation Memory
- [ ] FastAPI Backend
- [ ] React Frontend


## Supported Sources

| Source | Status |
|----------|:------:|
| PDF | ✅ |
| DOCX | ✅ |
| TXT | ✅ |
| Markdown | ✅ |
| PPTX | ✅ |
| Images | ✅ |
| Website URLs | ✅ |
| YouTube Videos | ✅ |