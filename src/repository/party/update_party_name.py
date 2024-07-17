from fastapi import APIRouter, HTTPException
from src.api.v1.update import update

router = APIRouter()

@router.post("/update-party-name")
def update_party_name(party_id: str, new_name: str):
    try:
        update("PARTY", party_id, {"name": new_name})
        return {"success": True, "message": "파티 이름 업데이트에 성공했습니다."}
    except Exception as e:
        return HTTPException(False, f"파티 이름 업데이트에 실패했습니다. {str(e)}")
        