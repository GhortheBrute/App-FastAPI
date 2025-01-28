from datetime import datetime, UTC

from pydantic import BaseModel


class PostOut(BaseModel):
    title: str
    data: datetime