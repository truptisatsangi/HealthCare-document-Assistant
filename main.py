from fastapi import FastAPI, UploadFile, File, HTTPException
from pypdf import PdfReader
from io import BytesIO


app = FastAPI()

@app.post("/upload")
async def upload_pdf(file: UploadFile = File(...)):
    # Validate file type
    if file.content_type != "application/pdf":
        raise HTTPException(status_code=404, detail="File type not supported")
    
    # Read uploaded PDF
    pdf_bytes = await file.read()
    pdf_reader = PdfReader(BytesIO(pdf_bytes))

    # Extract Text
    extracted_text = ""
    for page in pdf_reader.pages:
        extracted_text += page.extract_text() or ""

    return {
        "filename": file.filename,
        "pages": len(pdf_reader.pages),
        "text": extracted_text
    }

############################################################################################################


