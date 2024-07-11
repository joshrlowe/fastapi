from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional

app = FastAPI()


class Post(BaseModel):
    title: str
    content: str
    published: bool = True
    rating: Optional[int] = None


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/posts")
def get_posts():
    return {"data": "These are your posts"}


@app.post("/posts")
def create_posts(post: Post):
    print(post)
    print(post.dict())
    return {
        "data": f"title: '{post.title}', body: '{post.content}', published: {post.published}, rating: {post.rating}"
    }
