import os
import streamlit as st

from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter

from langchain_ollama import OllamaEmbeddings
from langchain_community.chat_models import ChatOllama

from langchain_community.vectorstores import FAISS

from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough

PDF_FOLDER = "pdfs"
VECTOR_DIR = "vectorstore"
MODEL = "llama3"

# Load PDFs

def load_documents():

    documents = []

    for file in os.listdir(PDF_FOLDER):

        if file.endswith(".pdf"):

            path = os.path.join(PDF_FOLDER, file)

            loader = PyPDFLoader(path)

            docs = loader.load()

            documents.extend(docs)

    return documents


# Split text
def split_docs(docs):

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=50
    )

    return splitter.split_documents(docs)


# Vector DB
def create_vector_db():

    embeddings = OllamaEmbeddings(model=MODEL)

    if os.path.exists(VECTOR_DIR):

        db = FAISS.load_local(
            VECTOR_DIR,
            embeddings,
            allow_dangerous_deserialization=True
        )

    else:

        docs = load_documents()

        chunks = split_docs(docs)

        db = FAISS.from_documents(chunks, embeddings)

        db.save_local(VECTOR_DIR)

    return db

# Build RAG
def build_rag_chain(db):

    retriever = db.as_retriever(search_kwargs={"k":3})

    prompt = ChatPromptTemplate.from_template("""Use the context to answer the question. Context: {context} Question: {question} """)

    llm = ChatOllama(model=MODEL)

    rag_chain = (
        {
            "context": retriever,
            "question": RunnablePassthrough()
        }
        | prompt
        | llm
        | StrOutputParser()
    )

    return rag_chain


# Streamlit UI
st.title("Enterprise AI Document Assistant")

st.write("Ask questions from your PDFs.")


if "history" not in st.session_state:
    st.session_state.history = []


db = create_vector_db()

rag_chain = build_rag_chain(db)


question = st.text_input("Ask your question")


if question:

    answer = rag_chain.invoke(question)

    st.session_state.history.append(("You", question))
    st.session_state.history.append(("Assistant", answer))


for role, msg in st.session_state.history:

    if role == "You":
        st.markdown(f"*You:** {msg}")

    else:
        st.markdown(f"**AI:** {msg}")