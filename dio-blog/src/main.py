from contextlib import asynccontextmanager

from fastapi import FastAPI

from src.controllers import post, auth
from database import *


@asynccontextmanager
async def lifespan(app: FastAPI):
    from src.models.post import posts  # noqa

    await database.connect()
    metadata.create_all(engine)
    yield
    await database.disconnect()


app = FastAPI(lifespan=lifespan)
app.include_router(post.router)
app.include_router(auth.router)


@app.get("/")
def read_root():
    return {"Hello": "World"}
