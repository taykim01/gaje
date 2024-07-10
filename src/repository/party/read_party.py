from fastapi import APIRouter
from api.v1 import read
from repository.party.party import PartyModel
from response import Response

router = APIRouter()

@router.get("/read-party", response_model=Response)
async def read_party(party_id: str) -> Response:
    try:
        response = await read("party", party_id)
        data = response.data[0] if response.data else None
        if not data:
            return Response(False, "파티 읽기에 실패했습니다.").to_dict()
        
        party_data = PartyModel(
            created_at=data['created_at'],
            name=data['name'],
            date_list=data['date_list'],
            id=data['id']
        ).to_dict()
        
        return Response(True, "파티 읽기에 성공했습니다.", party_data).to_dict()
    except Exception as e:
        return Response(False, "파티 읽기에 실패했습니다.", str(e)).to_dict()