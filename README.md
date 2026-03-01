# 📄 PDF-Based RAG System Using Local LLM (Ollama + LangChain)

This project implements a **Retrieval-Augmented Generation (RAG)** system that allows users to ask questions from PDF documents using a **local AI model**.

It uses **Ollama + LLaMA3**, so no paid API is required.

---

## 🚀 Project Objective

The goal of this project is to:

- Load PDF documents
- Split text into chunks
- Convert text into embeddings
- Store vectors in FAISS
- Retrieve relevant content
- Generate answers using a local LLM

This enables AI to answer questions from **private documents** securely.

---

## 🧠 Project Architecture (RAG Flow)


PDF → Text Split → Embeddings → FAISS → Retriever → LLM → Answer


---

## ⚙️ Prerequisites

Make sure your system has:

- Python 3.9 or above
- Minimum 8GB RAM (recommended)
- Internet (for setup only)

---

## 📥 Step 1: Install Python

Download Python from:

https://www.python.org/downloads/

During installation:

✔️ Select **Add Python to PATH**  
✔️ Click Install

Check installation:

```bash
python --version
📥 Step 2: Install Ollama (Local LLM)

Ollama allows you to run AI models locally.

Download Ollama

Search on Google:

Ollama Download

Or visit:

https://ollama.com

Download and install for your OS.

Verify Installation
ollama --version
📥 Step 3: Download LLaMA3 Model

After installing Ollama, run:

ollama pull llama3

Check:

ollama list

You should see llama3.

📁 Step 4: Clone the Repository
git clone https://github.com/your-username/your-repo-name.git
cd your-repo-name

(Replace with your actual repo link)

🐍 Step 5: Create Virtual Environment (Recommended)
Windows
python -m venv venv
venv\Scripts\activate
Linux / Mac
python3 -m venv venv
source venv/bin/activate
📦 Step 6: Install Required Packages

Run:

pip install -U pip

pip install langchain
pip install langchain-community
pip install langchain-text-splitters
pip install langchain-ollama
pip install faiss-cpu
pip install pypdf
📄 Step 7: Add PDF File

Place your PDF file in the project folder.

Rename it as:

data.pdf

Example structure:

project/
 ├── Rag_pdf_local.py
 ├── data.pdf
 └── venv/
▶️ Step 8: Start Ollama Server

Run:

ollama serve

Keep this terminal open.

▶️ Step 9: Run the Project

Open a new terminal.

Activate venv again and run:

python Rag_pdf_local.py
💬 Step 10: Ask Questions

After running, you will see:

RAG pipeline ready. You can ask now.

Example:

Ask: What is this document about?
Ask: Give me summary
Ask: Explain chapter 1

To exit:

exit

📈 Features

✅ PDF Loading
✅ Text Chunking
✅ Local Embeddings
✅ FAISS Storage
✅ Local LLM
✅ No API Cost
✅ Private Data Support

📌 Tech Stack

Python

LangChain

FAISS

Ollama

LLaMA3

PyPDF

👨‍💻 Author

Developed by: Venkataramana

AI & Machine Learning Enthusiast
Focused on RAG & LLM Systems

⭐ Future Improvements

Multi-PDF Support

Web Interface

Chat Memory

Cloud Deployment

📜 License

This project is for educational and learning purposes.
