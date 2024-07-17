from datetime import datetime
from fastapi import APIRouter, HTTPException
from src.repository.party.party import Party
from src.api.v1.create import create
from src.util import get_dates_in_range

router = APIRouter()

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
