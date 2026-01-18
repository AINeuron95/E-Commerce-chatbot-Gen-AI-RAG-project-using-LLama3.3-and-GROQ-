# E-Commerce-chatbot-Gen-AI-RAG-project-using-LLama3.3-and-GROQ-
This project is a Proof of Concept (PoC) for an intelligent e-commerce chatbot that enables natural, accurate, and real-time user interactions.
The chatbot identifies user intent using semantic routing and responds by either retrieving information from a vector database or executing LLM-generated SQL queries on a live database.

The system is designed using a Retrieval-Augmented Generation (RAG) architecture and can be extended to production-scale e-commerce platforms.

<img width="1913" height="915" alt="image" src="https://github.com/user-attachments/assets/1cbdd8ff-20f1-419a-af47-9c1fd9d98a5c" />

✨ Key Features

🧠 Semantic Intent Detection using a Semantic Router

📚 FAQ handling via Vector Database for fast semantic retrieval

🌐 Web scraping pipeline to collect product data

📄 Scraped data stored as CSV and ingested into SQLite

🗄️ LLM-powered SQL generation for real-time product queries

🤖 Llama-3.3 via GROQ for high-performance inference

⚡ Interactive UI built with Streamlit

Supported Intents

The chatbot currently supports two primary user intents, identified using semantic routing:

1️⃣ FAQ Intent (Vector Search)

Triggered when users ask platform-related or policy questions.

Examples:

Is online payment available?

What is the return policy?

👉 Implemented using:

Text embeddings

Vector database

Semantic similarity search

2️⃣ SQL Intent (Real-Time Product Search)

Triggered when users request product listings or filters.

Examples:

Show me all Nike shoes below Rs. 3000

List smartphones with 5G under Rs. 20,000

👉 Implemented using:

Web-scraped product data

CSV → SQLite database

LLM-generated SQLite queries

Secure query execution

🏗️ Architecture

<img width="1916" height="705" alt="image" src="https://github.com/user-attachments/assets/58ee466f-72d1-4ca8-b312-f9d4dbee7965" />

High-Level Flow:

User enters a query

Semantic Router determines intent

Based on intent:

FAQ → Vector DB retrieval

SQL → LLM generates SQLite query

Retrieved results are passed to Llama-3.3

Final answer returned to the user via Streamlit UI
