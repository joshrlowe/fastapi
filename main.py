from fastapi import FastAPI
from fastapi.params import Body

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/posts")
def get_posts():
    return {"data": "These are your posts"}


@app.post("/posts")
def create_post(payLoad: dict = Body(...)):
    print(payLoad)
    return {"new_post": f"title: '{payLoad['title']}', body: '{payLoad['content']}'"}
