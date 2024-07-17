from fastapi import HTTPException
from fastapi.encoders import jsonable_encoder
from src.service.supabase.db import db


def update(table_name: str, id: int, update_data: dict):
    try:
        update_data = jsonable_encoder(update_data, exclude_unset=True)
        db.table(table_name).update(update_data).eq("id", id).execute()
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
