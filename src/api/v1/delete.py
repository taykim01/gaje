from src.service.supabase import db
from src.response import Response


async def delete(table_name: str, id: int) -> Response:
    try:
        await (db.table(table_name).delete().eq("id", id).execute())
        return Response(True, "DB에 정보를 삭제하는데 성공했습니다.").to_dict()
    except Exception as e:
        return Response(False, "DB에 정보를 삭제하는데 실패했습니다.").to_dict()
