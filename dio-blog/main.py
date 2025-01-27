from datetime import datetime
from typing import Union

from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/posts/{framework}")
def read_framework_posts(framework: str):
    return {
        "posts": [
            {"title": f"Criando uma aplicação com {framework}", "data": datetime.now()},
            {"title": f"Internacionalizando uma app {framework}", "data": datetime.now()},
        ]
    }