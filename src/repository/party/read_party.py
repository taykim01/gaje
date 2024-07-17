import json
from fastapi import APIRouter, HTTPException
from src.api.v1.read import read
from src.repository.party.party import Party

router = APIRouter()


@router.get("/read-party/party_id={party_id}")
def read_party(party_id: str):
    try:
        response = read("PARTY", party_id).model_dump_json()
        response = json.loads(response)
        
        data = response["data"]

        party_data = Party(
            id=str(data["id"]),
            created_at=data["created_at"],
            name=data["name"],
            date_list=data["date_list"],
        )

        return party_data
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"파티 읽기에 실패했습니다. {str(e)}")
