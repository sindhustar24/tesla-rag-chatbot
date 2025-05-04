import os
from pypdf import PdfReader
from langchain_community.document_loaders import WebBaseLoader

def load_pdf_documents(pdf_directory):
    documents = []
    for filename in os.listdir(pdf_directory):
        if filename.endswith(".pdf"):
            path = os.path.join(pdf_directory, filename)
            reader = PdfReader(path)
            text = "\n".join([page.extract_text() for page in reader.pages])
            metadata = {"source": path, "type": "manual"}
            documents.append({"text": text, "metadata": metadata})
    return documents

def load_web_documents(urls):
    loader = WebBaseLoader(urls)
    return loader.load()