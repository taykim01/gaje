from fastapi import APIRouter
from api.v1 import update
from response import Response

router = APIRouter()

@router.get("/read-party", response_model=Response)
async def update_party_name(party_id: str, new_name: str):
    try:
        await update("party", party_id, {"name": new_name})
        return Response(True, "파티 이름 업데이트에 성공했습니다.").to_dict()
    except:
        return Response(False, "파티 이름 업데이트에 실패했습니다.").to_dict()