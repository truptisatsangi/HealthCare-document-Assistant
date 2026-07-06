from uuid import UUID
from pydantic import BaseModel
from datetime import date, datetime

from enums import reportType

class ReportMetadata(BaseModel):
    document_id: UUID
    patient_id: int
    filename: str
    report_type: reportType      
    referred_by: str
    hospital_name: str | None = None
    report_date: date | None = None
    upload_time: datetime
    page_count: int | None = None




