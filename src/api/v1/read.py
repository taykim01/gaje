from src.service.supabase import db
from src.response import Response


async def read_all(table_name: str) -> Response:
    try:
        response = await db.table(table_name).select("*").execute()
        return Response(True, "DB에 정보를 불러오는데 성공했습니다.", response).to_dict()
    except Exception as e:
        return Response(False, "DB에 정보를 불러오는데 실패했습니다.").to_dict()
    
    
async def read_by_id(table_name: str, id: int) -> Response:
    try:
        response = await db.table(table_name).select("*").eq("id", id).single()
        return Response(True, "DB에 정보를 불러오는데 성공했습니다.", response).to_dict()
    except Exception as e:
        return Response(False, "DB에 정보를 불러오는데 실패했습니다.").to_dict()
    
    
async def read_by_name(table_name: str, name: int) -> Response:
    try:
        response = await db.table(table_name).select("*").eq("name", name).single()
        return Response(True, "DB에 정보를 불러오는데 성공했습니다.", response).to_dict()
    except Exception as e:
        return Response(False, "DB에 정보를 불러오는데 실패했습니다.").to_dict()