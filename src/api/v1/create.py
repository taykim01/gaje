from fastapi import HTTPException
from fastapi.encoders import jsonable_encoder
from src.service.supabase.db import db


def create(table_name, data):
    try:
        data = jsonable_encoder(data, exclude_unset=True)
        db.table(table_name).insert(data).execute()
        return {
            "success": True,
            "message": "데이터 생성에 성공했습니다."
        }
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"데이터 생성에 실패했습니다. {str(e)}")