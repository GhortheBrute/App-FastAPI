from fastapi import status, APIRouter, Depends

from schemas.post import PostIn, PostUpdateIn
from services.post import PostService
from views.post import PostOut
from security import login_required

router = APIRouter(prefix="/posts", tags=["posts"], dependencies=[Depends(login_required)])

service = PostService()

@router.get("/", response_model=list[PostOut])
async def read_posts(published: bool, limit: int, skip: int = 0):
    return await service.read_all(published=published, limit=limit, skip=skip)


@router.get("/{id}", response_model=PostOut)
async def read_post(id: int):
    return await service.read(id)


@router.post("/", status_code=status.HTTP_201_CREATED, response_model=PostOut)
async def create_posts(post: PostIn):
    return {**post.model_dump(), "id": await service.create(post)}


@router.patch("/{id}", response_model=PostOut)
async def update_post(post: PostUpdateIn, id: int):
    return await service.update(id=id, post=post)


@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT, response_model=None)
async def delete_post(id: int):
    await service.delete(id)