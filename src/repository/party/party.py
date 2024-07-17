from typing import List, Optional
from datetime import datetime
from pydantic import BaseModel

class TimeSlot(BaseModel):
    date: str
    time: str
    users: List[str] = []
    unavailable: List[str] = []

class Party(BaseModel):
    id: Optional[str] = None
    created_at: datetime = None
    name: str
    date_list: List[TimeSlot] = []
    
    class Config:
        arbitrary_types_allowed = True