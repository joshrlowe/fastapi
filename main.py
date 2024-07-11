from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional

app = FastAPI()


class Post(BaseModel):
    title: str
    content: str
    published: bool = True
    rating: Optional[int] = None


my_posts = [
    {"title": "title of post 1", "conetnt": "content of post 1", "id": 1},
    {"title": "title of post 2", "conetnt": "content of post 2", "id": 2},
]


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/posts")
def get_posts():
    return {"data": my_posts}


@app.post("/posts")
def create_posts(post: Post):
    print(post)
    print(post.dict())
    return {
        "data": f"title: '{post.title}', body: '{post.content}', published: {post.published}, rating: {post.rating}"
    }
