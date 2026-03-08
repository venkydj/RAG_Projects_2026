AI Document Intelligence Assistant

This project is an AI-powered document chatbot that allows users to ask questions from PDF documents and get intelligent answers.

Instead of reading long documents manually, you can simply upload PDFs and ask questions, and the AI will find the answer from the document content.

The system uses a local AI model, so your documents stay private and secure on your computer.

🚀 Project Summary

This project builds a Retrieval-Augmented Generation (RAG) system that works in the following way:

The system loads one or more PDF documents.

The content of the PDFs is divided into small text chunks.

Each chunk is converted into numerical vectors (embeddings).

These vectors are stored in a vector database.

When a user asks a question, the system finds the most relevant content.

The AI model reads that content and generates an answer.

This allows the AI to understand and answer questions from documents.

🧠 Technologies Used

This project uses the following technologies:

Python

LangChain

Ollama

Llama 3

FAISS

Streamlit

These tools help build a local AI system that runs completely on your computer.

📂 Project Structure

Your project folder should look like this:

rag-pdf-chatbot/

app.py
requirements.txt

pdfs/
    sample.pdf

vectorstore/

app.py → Main application code

requirements.txt → Python packages needed

pdfs/ → Folder where you place your PDF documents

vectorstore/ → Stores AI search database (auto-generated)

⚙️ System Requirements

Before running this project, make sure your system has:

Python 3.9 or higher

Minimum 8 GB RAM (recommended)

Internet connection (only needed for setup)

📥 Step 1: Install Python

Download Python from the official website:

https://www.python.org/downloads/

During installation:

✔ Select Add Python to PATH
✔ Click Install

Verify installation:

python --version
📥 Step 2: Install Ollama (Local AI Model Runner)

This project uses Ollama to run AI models locally.

Install Ollama

Go to:

https://ollama.com

Download and install Ollama for your operating system.

Verify installation:

ollama --version
📥 Step 3: Download the AI Model

After installing Ollama, download the Llama 3 model.

Run this command:

ollama pull llama3

Check installed models:

ollama list

You should see llama3 in the list.

📥 Step 4: Download the Project

Clone the repository from GitHub:

git clone https://github.com/venkydj/RAG_Projects_2026.git

Move into the project folder:

cd rag-pdf-chatbot

Step 5: Create a Virtual Environment (Recommended)
Windows
python -m venv venv

venv\Scripts\activate

Mac / Linux

python3 -m venv venv

source venv/bin/activate

📦 Step 6: Install Required Packages

Install all required Python libraries:

pip install -r requirements.txt

These packages include tools like LangChain and FAISS.

📄 Step 7: Add Your PDF Files

Place the PDF documents you want to analyze inside the pdfs folder.

Example:

pdfs/

report.pdf
book.pdf
notes.pdf

The AI will read and analyze these documents.

▶️ Step 8: Start Ollama

Before running the application, start the Ollama service.

ollama serve

Keep this terminal open.

▶️ Step 9: Run the Application

Open a new terminal and run:

streamlit run app.py
🌐 Step 10: Open the Web Interface

After running the command, the browser will automatically open:

http://localhost:8501

You will see the application interface.

💬 Step 11: Ask Questions

In the application:

Type your question in the input box.

Click Ask.

The AI will search the documents and generate an answer.

Example questions:

"What is the main topic of this document?"

"Summarize the key points."

"What does the document say about machine learning?"

🔒 Privacy Advantage

This system runs completely locally using Ollama.

This means:

No paid API required

No data sent to external servers

Your documents remain private

📌 Key Features

✔ Ask questions from PDFs
✔ Supports multiple documents
✔ Local AI model (no API cost)
✔ Semantic document search
✔ Web interface using Streamlit
✔ Vector search using FAISS

🎯 Use Cases

This project can be used for:

Research paper analysis

Document summarization

Knowledge base assistants

Internal company documentation search

Study and learning tools

👨‍💻 Author

Venkataramana Podugu