# 📄 PDF Query using LangChain, Astra DB & Groq

An end-to-end Retrieval-Augmented Generation (RAG) application that allows users to upload PDF documents and ask natural language questions about their content.

The application extracts text from PDFs, converts it into vector embeddings using Hugging Face, stores them in Astra DB, retrieves the most relevant chunks for a user query, and generates accurate answers using Groq's Llama 3.3 model.

---

## 🚀 Features

- 📄 Upload any PDF document
- ✂️ Automatic document chunking
- 🧠 Hugging Face Embeddings
- 🗄️ Astra DB Vector Database
- 🔍 Semantic Search
- 🤖 Groq Llama 3.3-70B LLM
- ⚡ Fast Retrieval-Augmented Generation (RAG)
- 💬 Interactive Streamlit Interface

---

## 🛠️ Tech Stack

- Python
- Streamlit
- LangChain
- Hugging Face Embeddings
- Astra DB Vector Store
- Groq API
- Llama 3.3 70B Versatile
- PyPDFLoader

---

## 📂 Project Structure

```
PDF_Query/
│
├── app.py
├── requirements.txt
├── .env
├── README.md
└── sample.pdf
```

---

## ⚙️ Architecture

```
                User Uploads PDF
                       │
                       ▼
               PyPDFLoader
                       │
                       ▼
      Recursive Character Splitter
                       │
                       ▼
        HuggingFace Embeddings
                       │
                       ▼
          Astra DB Vector Store
                       │
                       ▼
               Retriever (Top-K)
                       │
                       ▼
           LangChain Retrieval Chain
                       │
                       ▼
         Groq Llama-3.3-70B LLM
                       │
                       ▼
                Final Response
```

---

## 🧩 Workflow

### Step 1
Upload a PDF document through the Streamlit interface.

### Step 2
The PDF is loaded using **PyPDFLoader**.

### Step 3
The document is split into smaller chunks using **RecursiveCharacterTextSplitter**.

### Step 4
Each chunk is converted into embeddings using

```
sentence-transformers/all-MiniLM-L6-v2
```

### Step 5
The embeddings are stored inside **Astra DB**.

### Step 6
When a user asks a question, the retriever searches for the most relevant chunks.

### Step 7
The retrieved context and user query are passed to **Groq Llama 3.3-70B**.

### Step 8
The LLM generates an answer grounded in the retrieved document content.

---

## 🔑 Environment Variables

Create a `.env` file.

```env
GROQ_API_KEY=your_groq_api_key

ASTRA_DB_API_ENDPOINT=your_astra_endpoint

ASTRA_DB_APPLICATION_TOKEN=your_astra_token
```

---

## 📦 Installation

Clone the repository

```bash
git clone https://github.com/yourusername/pdf-query-rag.git
```

Move into the project directory

```bash
cd pdf-query-rag
```

Create a virtual environment

```bash
python -m venv venv
```

Activate the virtual environment

### Windows

```bash
venv\Scripts\activate
```

### Linux / macOS

```bash
source venv/bin/activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

Run the application

```bash
streamlit run app.py
```

---

## 📚 LangChain Components Used

- PyPDFLoader
- RecursiveCharacterTextSplitter
- HuggingFaceEmbeddings
- AstraDBVectorStore
- ChatPromptTemplate
- create_stuff_documents_chain
- create_retrieval_chain
- ChatGroq

---

## 🧠 Embedding Model

```
sentence-transformers/all-MiniLM-L6-v2
```

---

## 🤖 LLM

```
llama-3.3-70b-versatile
```

Powered by **Groq**.

---

## 📈 Future Improvements

- Support multiple PDF uploads
- Chat history memory
- Source citation for retrieved chunks
- Streaming responses
- Hybrid search
- Metadata filtering
- PDF summarization
- Multi-document RAG
- Image extraction from PDFs
- Agentic RAG using LangGraph

---

## 🎯 Learning Outcomes

This project demonstrates:

- Retrieval-Augmented Generation (RAG)
- Vector Databases
- Semantic Search
- Document Chunking
- Embedding Models
- LangChain Pipelines
- Prompt Engineering
- Groq LLM Integration
- Astra DB Integration
- Streamlit Deployment

---

## 👨‍💻 Author

**Vivek Pobbathi**

B.Tech – Computer Science & Engineering

Passionate about AI, Generative AI, LLMs, RAG, Agentic AI, and Full Stack Development.

---

## ⭐ If you found this project useful, consider giving it a star!
