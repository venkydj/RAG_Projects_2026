import os
# PDF loader
from langchain_community.document_loaders import PyPDFLoader
# Text splitter
from langchain_text_splitters import RecursiveCharacterTextSplitter
#Embedding model (local)
from langchain_ollama import OllamaEmbeddings
#Vector DB
from langchain_community.vectorstores import FAISS
# Local LLM
from langchain_community.chat_models import ChatOllama

# Prompt builder
from langchain_core.prompts import ChatPromptTemplate

# Core runnable logic
from langchain_core.runnables import RunnablePassthrough
from langchain_core.output_parsers import StrOutputParser

print("\nLoading PDF...")

# LOAD PDF
loader = PyPDFLoader("data.pdf")
docs = loader.load()

print("PDF loaded into memory.")

#SPLIT TEXT
splitter = RecursiveCharacterTextSplitter(
    chunk_size=500,
    chunk_overlap=50
)

chunks = splitter.split_documents(docs)
print("Text split into chunks:", len(chunks))

#EMBEDDINGS
embeddings = OllamaEmbeddings(model="llama3")
print("Embeddings engine ready.")

# VECTOR DATABASE
db = FAISS.from_documents(chunks, embeddings)
retriever = db.as_retriever()
print("Vector DB ready. Retriever built.")

#PROMPT TEMPLATE
prompt = ChatPromptTemplate.from_template("""
Answer ONLY using the provided CONTEXT.

Context:
{context}

Question:
{question}
""")

print("Prompt template ready.")

#LOCAL LLM (Ollama)
llm = ChatOllama(model="llama3")
print("Local LLM ready.")

#BUILD RAG RUNNABLE PIPELINE

rag_chain = (
    {
        "context": retriever,
        "question": RunnablePassthrough()
    }
    | prompt
    | llm
    | StrOutputParser()
)

print("RAG pipeline ready. You can ask now.")

#CHAT LOOP
while True:
    q = input("\nAsk (type 'exit' to stop): ")
    if q.lower() == "exit":
        break

    out = rag_chain.invoke(q)
    print("\nAnswer:\n", out)
    print("-" * 60)