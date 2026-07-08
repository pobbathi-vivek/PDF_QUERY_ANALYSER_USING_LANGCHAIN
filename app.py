import os
from dotenv import load_dotenv
import streamlit as st

from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter

from langchain_huggingface import HuggingFaceEmbeddings
from langchain_astradb import AstraDBVectorStore
from langchain_groq import ChatGroq

from langchain_core.prompts import ChatPromptTemplate
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain.chains.retrieval import create_retrieval_chain


# ----------------------------
# Load Environment Variables
# ----------------------------

load_dotenv()

GROQ_API_KEY = os.getenv("GROQ_API_KEY")
ASTRA_DB_API_ENDPOINT = os.getenv("ASTRA_DB_API_ENDPOINT")
ASTRA_DB_APPLICATION_TOKEN = os.getenv("ASTRA_DB_APPLICATION_TOKEN")


# ----------------------------
# Streamlit UI
# ----------------------------

st.set_page_config(
    page_title="PDF Query using LangChain",
    page_icon="📄",
    layout="wide"
)

st.title("📄 PDF Query using LangChain + Groq + Astra DB")

pdf = st.file_uploader(
    "Upload PDF",
    type="pdf"
)

# ----------------------------
# Process PDF
# ----------------------------

if pdf is not None:

    with open(pdf.name, "wb") as f:
        f.write(pdf.getbuffer())

    loader = PyPDFLoader(pdf.name)

    documents = loader.load()

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=200
    )

    docs = splitter.split_documents(documents)

    embedding = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )

    vectorstore = AstraDBVectorStore(
        collection_name="pdf_query",
        embedding=embedding,
        api_endpoint=ASTRA_DB_API_ENDPOINT,
        token=ASTRA_DB_APPLICATION_TOKEN,
    )

    with st.spinner("Uploading documents to Astra DB..."):

        vectorstore.delete_collection()

        vectorstore = AstraDBVectorStore(
            collection_name="pdf_query",
            embedding=embedding,
            api_endpoint=ASTRA_DB_API_ENDPOINT,
            token=ASTRA_DB_APPLICATION_TOKEN,
        )

        vectorstore.add_documents(docs)

    st.success("PDF Indexed Successfully")

    retriever = vectorstore.as_retriever(
        search_kwargs={"k":3}
    )

    llm = ChatGroq(
        groq_api_key=GROQ_API_KEY,
        model_name="llama-3.3-70b-versatile"
    )

    prompt = ChatPromptTemplate.from_template(
    """
    Answer the question based only on the provided context.

    <context>
    {context}
    </context>

    Question:
    {input}
    """
    )

    document_chain = create_stuff_documents_chain(
        llm,
        prompt
    )

    retrieval_chain = create_retrieval_chain(
        retriever,
        document_chain
    )

    question = st.text_input("Ask a Question")

    if question:

        with st.spinner("Generating Answer..."):

            response = retrieval_chain.invoke(
                {
                    "input": question
                }
            )

        st.subheader("Answer")

        st.write(response["answer"])