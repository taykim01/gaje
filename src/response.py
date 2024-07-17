from typing import Union
from pydantic import BaseModel

class Response(BaseModel):
    success: bool
    message: str
    data: Union[dict, list] | None = None
