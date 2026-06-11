import os
from langchain_community.document_loaders import PyPDFLoader, TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter

def load_and_split_docs(file_path, chunk_size=500, chunk_overlap=50):
    if file_path.endswith('.pdf'):
        loader = PyPDFLoader(file_path)
    else:
        loader = TextLoader(file_path)
    docs = loader.load()
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=chunk_size, chunk_overlap=chunk_overlap)
    return text_splitter.split_documents(docs)