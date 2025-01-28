from datetime import datetime
from typing import Annotated

from fastapi import Response, Cookie, status, Header, APIRouter

from schemas.post import PostIn
from views.post import PostOut

router = APIRouter(prefix="/posts", tags=["posts"])

fake_db = [
    {"title": f"Criando uma aplicação com FastAPI", "data": datetime.now(),"published": True},
    {"title": f"Internacionalizando uma app Django", "data": datetime.now(), "published": True},
    {"title": f"Internacionalizando uma app Flask", "data": datetime.now(), "published": True},
    {"title": f"Internacionalizando uma app Pandas", "data": datetime.now(), "published": False},
]


@router.get("/{framework}", response_model=PostOut)
def read_framework_posts(framework: str):
    return {
        "posts": [
            {"title": f"Criando uma aplicação com {framework}", "data": datetime.now()},
            {"title": f"Internacionalizando uma app {framework}", "data": datetime.now()},
        ]
    }


@router.get("/", response_model=list[PostOut])
def read_posts(response: Response, published: bool, limit: int, skip: int = 0, ads_id: Annotated[str | None, Cookie()] = None,
               user_agent: Annotated[str | None, Header()] = None,):
    response.set_cookie(key='user', value='eitaro1@gmail.com')
    print(f"Cookie: {ads_id}")
    print(f"UserAgent: {user_agent}")
    return [post for post in fake_db[skip : skip + limit] if post["published"] is published]


@router.post("/", status_code=status.HTTP_201_CREATED, response_model=PostOut)
def create_posts(post: PostIn):
    fake_db.append(post.model_dump())
    return post