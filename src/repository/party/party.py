from typing import List, Optional
from datetime import datetime


class TimeSlot:
    def __init__(self, date: str, time: str, users: List[str], unavailable: List[str]):
        self.date = date
        self.time = time
        self.users = users
        self.unavailable = unavailable

    def to_dict(self):
        return {
            "date": self.date,
            "time": self.time,
            "users": self.users,
            "unavailable": self.unavailable,
        }


class PartyModel:
    def __init__(
        self,
        created_at: datetime,
        name: str,
        date_list: List[TimeSlot],
        id: Optional[str] = None,
    ):
        self.created_at = created_at
        self.name = name
        self.date_list = date_list
        self.id = id

    def to_dict(self):
        return {
            "created_at": self.created_at,
            "name": self.name,
            "date_list": [slot.to_dict() for slot in self.date_list],
            "id": self.id,
        }
