from io import BytesIO
from fastapi import HTTPException, UploadFile
from pypdf import PdfReader
import uuid

class ReportService:
    """
    Responsible for validating and parsing uploaded medical reports.

    Responsibilities:
    - Validate uploaded file
    - Parse PDF
    - Extract text
    - Extract document metadata (page count, filename)
    """

    async def validate_report(self, file: UploadFile) -> None:
        """Validate uploaded report."""

        if file.content_type != "application/pdf":
            raise HTTPException(status_code=415, detail="Only PDF files are supported.")

        pdf_bytes = await file.read()

        if not pdf_bytes:
            raise HTTPException(status_code=400, detail="Uploaded file is empty.")

        try:
            PdfReader(BytesIO(pdf_bytes))
        except Exception:
            raise HTTPException(status_code=400, detail="Invalid or corrupted PDF.")

        # Reset file pointer after reading
        await file.seek(0)

    async def parse_report(self, file: UploadFile) -> dict:
        """Parse PDF and extract text + metadata."""

        pdf_bytes = await file.read()
        reader = PdfReader(BytesIO(pdf_bytes))

        text = "\n".join(page.extract_text() or "" for page in reader.pages)

        if not text.strip():
            raise HTTPException(
                status_code=400,
                detail="No extractable text found in the PDF."
            )

        await file.seek(0)

        return {
            "filename": file.filename or f"{uuid.uuid4()}.pdf",
            "page_count": len(reader.pages),
            "text": text,
        }