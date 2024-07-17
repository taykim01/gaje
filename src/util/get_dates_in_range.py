from datetime import datetime, timedelta
from typing import List
from repository.party.party import TimeSlot
from util import format_date, time_segments


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
    