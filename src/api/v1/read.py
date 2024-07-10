from src.service.supabase import db
from src.response import Response

async def read(table_name: str, id: int) -> Response:
    try:
        response = await db.table(table_name).select("*").eq("id", id).single()
        return Response(True, "DB에 정보를 불러오는데 성공했습니다.", response).to_dict()
    except Exception as e:
        return Response(False, "DB에 정보를 불러오는데 실패했습니다.").to_dict()