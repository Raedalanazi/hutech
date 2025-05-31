from pydantic import BaseModel
from typing import Optional

class Employee(BaseModel):
    id: int
    name: str
    position: str
    department: Optional[str] = None
    email: Optional[str] = None
