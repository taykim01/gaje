import json
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from src.api.v1.read import read
from src.api.v1.update import update
from src.repository.party.party import Party

router = APIRouter()

class JoinPartyRequest(BaseModel):
    party_id: str
    user_name: str
    available_slots: str

@router.post("/update-party-member")
def update_party_member(request: JoinPartyRequest):
    try:
        response = read("PARTY", request.party_id).model_dump_json()
        response = json.loads(response)
        data = response["data"]
        party_data = Party(
            id=str(data["id"]),
            created_at=data["created_at"],
            name=data["name"],
            date_list=data["date_list"],
        )
        date_list = party_data.date_list

        available_slots = json.loads(available_slots)

        user_available_time = []
        for slot in available_slots:
            for date in date_list:
                if slot["date"] == date.date:
                    if slot["time"] == date.time:
                        if request.user_name not in date.users:
                            date.users.append(request.user_name)
                        if request.user_name in date.unavailable:
                            date.unavailable.remove(request.user_name)
                user_available_time.append(date)

        update_payload = {"date_list": user_available_time}
        response = update("PARTY", request.model_dump_jsonparty_id, update_payload)

        return {"success": True, "message": "파티 멤버 업데이트에 성공했습니다."}
    except Exception as e:
        raise HTTPException(
            status_code=400, detail=f"파티 정보 업데이트에 실패했습니다. {str(e)}"
        )
