from datetime import datetime, UTC

from pydantic import BaseModel


class PostIn(BaseModel):
    title: str
    data: datetime = datetime.now(UTC)
    published: bool = False