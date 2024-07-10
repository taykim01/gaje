from src.service.supabase import db
from src.response import Response


async def update(table_name: str, id: int, update_data: dict) -> Response:
    try:
        await (db.table(table_name).update(update_data).eq("id", id).execute())
        return Response(True, "DB에 정보를 업데이트하는데 성공했습니다.").to_dict()
    except Exception as e:
        return Response(False, "DB에 정보를 업데이트하는데 실패했습니다.").to_dict()
