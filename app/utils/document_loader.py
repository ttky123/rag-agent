from langchain_community.document_loaders import PyPDFLoader
from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import HuggingFaceEmbeddings

def load_documents():
    
    loader1 = PyPDFLoader("data/guide.pdf")
    loader2 = PyPDFLoader("data/api_spec.pdf")
    docs1 = loader1.load()
    docs2 = loader2.load()
    all_docs = docs1 + docs2

    # sentence Transformer를 이용하여 문장 단위 임베딩
    embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
    vectorstore = FAISS.from_documents(all_docs, embeddings)
    vectorstore.save_local("vector_store")
    return vectorstore
