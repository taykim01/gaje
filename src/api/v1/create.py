from src.service.supabase import db
from src.response import Response


async def create(table_name: str, data: dict) -> Response:
    try:
        await db.table(table_name).insert(data).execute()
        return Response(True, "DB에 정보를 저장하는데 성공했습니다.").to_dict()
    except Exception as e:
        return Response(False, "DB에 정보를 등록하는데 실패했습니다.").to_dict()