from datetime import datetime
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from src.repository.party.party import Party
from src.api.v1.create import create
from src.util.get_dates_in_range import get_dates_in_range


router = APIRouter()

class PartyCreateRequest(BaseModel):
    name: str
    start_date: str
    end_date: str

@router.post("/create-party")
async def create_party(request: PartyCreateRequest):
    try:
        date_range = get_dates_in_range(request.start_date, request.end_date)
        new_party = Party(created_at=datetime.now(), name=request.name, date_list=date_range)
        response = create(table_name="PARTY", data=new_party)

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