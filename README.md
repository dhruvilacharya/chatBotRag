# Production-Ready RAG Chatbot with RedisVL

Welcome to the RedisVL RAG Chatbot project! This repository contains a two-part lab series designed to teach you how to build a Retrieval-Augmented Generation (RAG) pipeline from scratch and then upgrade it for production using semantic caching and conversational memory. 

The chatbot is built to analyze and answer questions based on **Nike's 2023 10-K Financial Filing**.

## 🚀 Project Overview

This project demonstrates how to leverage **Redis** as a vector database and **OpenAI** as the LLM engine to create an interactive, context-aware chatbot. 

### Key Features
* **Semantic Vector Search:** Embeds and indexes PDF document chunks in Redis.
* **Retrieval-Augmented Generation (RAG):** Grounds LLM responses in factual context retrieved from the financial document.
* **Semantic Caching:** Reduces LLM latency and costs by serving exact or semantically similar repeat queries directly from the cache.
* **Session Memory:** Maintains conversational history, allowing for multi-turn interactions.
* **Interactive UI:** A custom IPython widget-based chat interface.

## 📂 File Structure

* **`01_redisvl_basic_rag.ipynb`**: Lab 1 Notebook. Covers building a RAG pipeline from scratch, embedding the PDF data, and performing basic vector search.
* **`02_redisvl_production_rag.ipynb`**: Lab 2 Notebook. Enhances the RAG pipeline with semantic caching (using LangCache/RedisVL) and session memory.
* **`setup-lab-prod.py`**: A helper script that initializes the Redis connection, sets up the OpenAI API, defines the system prompt, and manages background pipeline functions.
* **`chat_ui.py`**: Contains the Python logic for the frontend interactive chat widget.
* **`chat_interface.py`**: Wraps the chat UI to interface with either the basic RAG function (Lab 1) or the advanced ChatBot instance (Lab 2).
* **`nke-10k-2023.pdf`**: The dataset. Nike's annual 10-K report for the fiscal year ended May 31, 2023.

## 🛠️ Setup and Installation

### Prerequisites
* A running **Redis** instance (local or cloud).
* An **OpenAI API Key**.
* Python 3.8+ with Jupyter Notebook / JupyterLab environment.

### Environment Variables
Ensure the following environment variables are set before running the notebooks:
* `REDIS_HOST` (default: localhost)
* `REDIS_PORT` (default: 6379)
* `REDIS_PASSWORD` (default: "")
* `OPENAI_API_KEY` (The setup scripts will securely prompt for this if not found).

## 🏃‍♂️ Getting Started

1. **Start with Lab 1:** Open `01_redisvl_basic_rag.ipynb`. Run through the cells to parse the Nike 10-K PDF, generate embeddings using HuggingFace sentence-transformers, load them into Redis, and test the basic LLM question-answering capabilities.
2. **Move to Lab 2:** Open `02_redisvl_production_rag.ipynb`. This notebook builds on the index created in Lab 1. You will implement caching to speed up recurring questions and add memory to handle follow-up questions seamlessly.
3. **Interact:** Use the built-in chat UI rendered at the end of the notebooks to talk to the financial data!

## 📚 Resources
* [RedisVL Documentation](https://github.com/redis/redis-vl-python)
* [Redis for AI](https://redis.io/docs/latest/develop/ai/)
* [OpenAI API](https://platform.openai.com/docs/)
