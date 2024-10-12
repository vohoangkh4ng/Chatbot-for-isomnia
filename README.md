# Insomnia Chatbot with Retrieval-Augmented Generation (RAG)

A **RAG-based chatbot** designed to provide comprehensive and personalized guidance on managing insomnia. This chatbot combines powerful document retrieval with generation capabilities, leveraging cutting-edge NLP models to help users improve their sleep habits.

## Table of Contents
1. [Overview](#overview)
2. [Features](#features)
3. [Project Structure](#project-structure)
4. [Installation](#installation)
5. [Usage](#usage)
6. [Detailed Workflow](#detailed-workflow)
7. [Future Enhancements](#future-enhancements)

---

## Overview

This chatbot leverages **Retrieval-Augmented Generation (RAG)** to answer insomnia-related questions by retrieving relevant content from a database of scientific articles and generating detailed, contextually relevant responses. The chatbot is designed to be an interactive, supportive tool for users who want to improve their sleep habits with evidence-based strategies.

## Features

- **Evidence-Based Guidance**: Provides users with scientifically-backed sleep improvement tips.
- **Semantic Search**: Utilizes dense and sparse embeddings to retrieve the most relevant content from a vector store.
- **Detailed Summarization**: Generates high-level summaries of scientific articles on insomnia, ensuring that each response is tailored to the user's specific needs.
- **Interactive Chatbot**: Engages users in meaningful conversations and offers advice based on their inputs.

---

## Project Structure

Here’s an overview of the key files and their functions:

```plaintext
├── extract_pdf.py                     # Extracts content from PDF files
├── retrieve_with_reranker.py          # Retrieves relevant content based on user queries with reranking
├── semantic_encoder.py                # Encodes documents into embeddings for semantic retrieval
├── semantic_chunking.py               # Divides documents into meaningful chunks and generates summaries
├── semantic_vectorstore.py            # Manages vector storage and embedding creation with Qdrant
├── utils/                             # Utility functions for chunking, embedding, etc.
└── README.md                          # Project documentation (this file)
```
## Installation

### Prerequisites

Ensure you have the following installed:

- Python 3.8+
- [Qdrant](https://qdrant.tech/)
- [Torch](https://pytorch.org/), [LangChain](https://github.com/hwchase17/langchain)
- Install additional dependencies with `pip`:

```bash
pip install -r requirements.txt
```
