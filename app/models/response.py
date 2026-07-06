from pydantic import BaseModel
from app.models.report_metadata import DocumentMetadata

from enums import Category

class Response(BaseModel):
    patient_id: int
    response: str
    category: Category
    source_metadata: list[DocumentMetadata]