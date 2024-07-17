from fastapi import HTTPException
from src.service.supabase.db import db


def delete(table_name: str, id: int):
    try:
        db.table(table_name).delete().eq("id", id).execute()
        return {"success": True, "message": "데이터 삭제에 성공했습니다."}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
