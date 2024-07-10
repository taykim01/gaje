from datetime import datetime, timedelta
from typing import List, Dict, Any
from response import Response
from src.repository.party.party import TimeSlot, PartyModel
import requests
from src.api.v1.create import create
from src.service.supabase.db import party_table

class CreatePartyUseCase:
    def __init__(self):
        self.time_segments = [
            "00:00~00:30", "00:30~01:00",
            "01:00~01:30", "01:30~02:00",
            "02:00~02:30", "02:30~03:00",
            "03:00~03:30", "03:30~04:00",
            "04:00~04:30", "04:30~05:00",
            "05:00~05:30", "05:30~06:00",
            "06:00~06:30", "06:30~07:00",
            "07:00~07:30", "07:30~08:00",
            "08:00~08:30", "08:30~09:00",
            "09:00~09:30", "09:30~10:00",
            "10:00~10:30", "10:30~11:00",
            "11:00~11:30", "11:30~12:00",
            "12:00~12:30", "12:30~13:00",
            "13:00~13:30", "13:30~14:00",
            "14:00~14:30", "14:30~15:00",
            "15:00~15:30", "15:30~16:00",
            "16:00~16:30", "16:30~17:00",
            "17:00~17:30", "17:30~18:00",
            "18:00~18:30", "18:30~19:00",
            "19:00~19:30", "19:30~20:00",
            "20:00~20:30", "20:30~21:00",
            "21:00~21:30", "21:30~22:00",
            "22:00~22:30", "22:30~23:00",
            "23:00~23:30", "23:30~24:00"
        ]

    def format_date(self, date: datetime) -> str:
        return date.strftime("%m/%d")

    def get_dates_in_range(self, start_date: str, end_date: str) -> List[Dict[str, Any]]:
        dates = []
        current_date = datetime.strptime(start_date, "%Y-%m-%d")
        end_date_in_date = datetime.strptime(end_date, "%Y-%m-%d")

        while current_date <= end_date_in_date:
            current_date_str = self.format_date(current_date)
            for time_segment in self.time_segments:
                time_slot = TimeSlot(
                    current_date_str,
                    time_segment,
                    [],
                    []
                ).to_dict()
                dates.append(time_slot)
            current_date += timedelta(days=1)

        return dates

    async def createParty(self, name: str, start_date: str, end_date: str) -> Response:
        try:
            created_at = datetime.now()
            date_range = self.get_dates_in_range(start_date, end_date)

            party_data = PartyModel(
                created_at,
                name,
                date_range
            ).to_dict()
            
            response = await create(party_table, party_data)

            if response.success:
                return Response(True, "DB에 파티를 생성하는데 성공했습니다")
            else:
                return Response(False, "DB에 파티를 생성하는데 실패했습니다.")
        except:
            return Response(False, "파티 생성에 실패했습니다.", {})