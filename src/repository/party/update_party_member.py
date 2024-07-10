from typing import List
from fastapi import APIRouter
from api.v1 import read, update
from repository.party.party import TimeSlot
from response import Response

router = APIRouter()

@router.get("/read-party", response_model=Response)
async def update_party_member(party_id: str, user_name: str, available_time: List[TimeSlot]) -> Response:
    try:
        response = await read("party", party_id)
        if not response.success:
            return Response(False, "파티 정보 읽기에 실패했습니다.", response.data)
        
        party_data = response.data
        date_list = party_data['date_list']

        user_available_time = []
        for time in available_time:
            date = time.date
            time_slot = next((slot for slot in date_list if slot['date'] == date), None)
            if not time_slot:
                return Response(False, "해당 날짜의 TimeSlot을 찾을 수 없습니다.", {})
            time_slot['users'].append(user_name)
            user_available_time.append(time_slot)

        update_payload = {
            'partyID': party_id,
            'partyData': {
                'userAvailableTime': user_available_time
            }
        }

        response = await update("party", party_id, update_payload)
        if not response.success:
            return Response(False, "파티 정보 업데이트에 실패했습니다.", response.data)
        
        return Response(True, "파티 정보 업데이트에 성공했습니다.")
    except Exception as e:
        return Response(False, "파티 정보 업데이트에 실패했습니다.", str(e))