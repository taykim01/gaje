from fastapi import HTTPException
from src.service.supabase.db import db
from src.response import Response


def read(table_name: str, id: int) -> Response:
    try:
        response = db.table(table_name).select("*").eq("id", id).single().execute()
        return response
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"데이터를 읽어오는데 실패했습니다. {str(e)}")
