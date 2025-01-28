from fastapi import FastAPI

from controllers import post
app = FastAPI()
app.include_router(post.router)



@app.get("/")
def read_root():
    return {"Hello": "World"}





