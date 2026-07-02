from fastapi import FastAPI, UploadFile, File, HTTPException
from pypdf import PdfReader
from io import BytesIO
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_openai import ChatOpenAI, OpenAIEmbeddings
from langchain_core.vectorstores import InMemoryVectorStore
from langchain_huggingface import HuggingFaceEmbeddings

import getpass
import os
import logging

if not os.environ.get("OPENAI_API_KEY"):
    os.environ["OPENAI_API_KEY"] = getpass.getpass("Enter API key for OpenAI: ")


app = FastAPI()
logger = logging.getLogger(__name__)

async def upload_pdf(file: UploadFile):
    # Validate file type
    if file.content_type != "application/pdf":
        raise HTTPException(status_code=415, detail="File type not supported")
    
    # Read uploaded PDF
    pdf_bytes = await file.read()
    pdf_reader = PdfReader(BytesIO(pdf_bytes))

    # Extract Text
    texts = []
    for page in pdf_reader.pages:
        texts.append(page.extract_text() or "")

    if len(texts) < 1:
        raise HTTPException(400, "No text found in PDF")
    
    return {
        "filename": file.filename,
        "pages": len(pdf_reader.pages),
        "text": "\n".join(texts)
    }


# Load and Chunk the data
def make_chunks(text):
    try:
        text_splitter = RecursiveCharacterTextSplitter(chunk_size = 500, chunk_overlap= 100)
        all_chunks = text_splitter.create_documents([text])
    
    except HTTPException:
        raise
    except Exception:
        logger.exception("Chunk creation failed")
        raise HTTPException(500, "Internal Server Error")
    
    return {
        "num_chunks": len(all_chunks),
        "chunks": all_chunks
    }


@app.post("/embedding")
async def embedding(file: UploadFile = File(...)):
    
    result  = await upload_pdf(file)
    chunks = make_chunks(result["text"])
    embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-mpnet-base-v2",
    encode_kwargs={"normalize_embeddings": True},
   )
    # embeddings = OpenAIEmbeddings(model="text-embedding-3-large")
    vector_store = InMemoryVectorStore(embeddings)
    document_Ids = vector_store.add_documents(documents=chunks["chunks"])
    print(document_Ids)
    return document_Ids





