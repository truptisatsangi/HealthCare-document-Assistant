from pydantic import BaseModel

from enums import Category

class UserQuery(BaseModel):
    patient_id: int
    query: str
    category: Category


