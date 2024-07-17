from datetime import datetime, timedelta
from typing import List
from fastapi import APIRouter, HTTPException
from src.repository.party.party import TimeSlot, Party
from src.api.v1.create import create

router = APIRouter()


time_segments = [
    "00:00~00:30",
    "00:30~01:00",
    "01:00~01:30",
    "01:30~02:00",
    "02:00~02:30",
    "02:30~03:00",
    "03:00~03:30",
    "03:30~04:00",
    "04:00~04:30",
    "04:30~05:00",
    "05:00~05:30",
    "05:30~06:00",
    "06:00~06:30",
    "06:30~07:00",
    "07:00~07:30",
    "07:30~08:00",
    "08:00~08:30",
    "08:30~09:00",
    "09:00~09:30",
    "09:30~10:00",
    "10:00~10:30",
    "10:30~11:00",
    "11:00~11:30",
    "11:30~12:00",
    "12:00~12:30",
    "12:30~13:00",
    "13:00~13:30",
    "13:30~14:00",
    "14:00~14:30",
    "14:30~15:00",
    "15:00~15:30",
    "15:30~16:00",
    "16:00~16:30",
    "16:30~17:00",
    "17:00~17:30",
    "17:30~18:00",
    "18:00~18:30",
    "18:30~19:00",
    "19:00~19:30",
    "19:30~20:00",
    "20:00~20:30",
    "20:30~21:00",
    "21:00~21:30",
    "21:30~22:00",
    "22:00~22:30",
    "22:30~23:00",
    "23:00~23:30",
    "23:30~24:00",
]


def format_date(date: datetime) -> str:
    return date.strftime("%Y-%m-%d")


def get_dates_in_range(start_date: str, end_date: str) -> List[TimeSlot]:
    dates = []
    current_date = datetime.strptime(start_date, "%Y-%m-%d")
    end_date_in_date = datetime.strptime(end_date, "%Y-%m-%d")

    while current_date <= end_date_in_date:
        current_date_str = format_date(current_date)
        for time_segment in time_segments:
            time_slot = TimeSlot(
                date=current_date_str, time=time_segment, users=[], unavailable=[]
            )
            dates.append(time_slot)
        current_date += timedelta(days=1)

    return dates


@router.post("/create-party")
async def create_party(name: str, start_date: str, end_date: str):
    try:
        date_range = get_dates_in_range(start_date, end_date)

        party = Party(created_at=datetime.now(), name=name, date_list=date_range)

        response = create(table_name="PARTY", data=party)

        if not response["success"]:
            raise HTTPException(
                status_code=400,
                detail=f"DB에 파티를 생성하는데 실패했습니다. {response['message']}",
            )
        else:
            return {"detail": "파티 생성에 성공했습니다."}
    except Exception as e:
        raise HTTPException(
            status_code=400, detail=f"파티 생성에 실패했습니다. Error: {str(e)}"
        )
