from typing import Optional
from fastapi import Body, FastAPI
from pydantic import BaseModel

app = FastAPI()

class Post(BaseModel):
    title: str
    content: str
    published: bool = True
    rating: Optional[int] = None


my_posts = [{"title": "top beaches on Florida",
            "content": "check out awesomae beches",
            "id": 1},
            {"title": "favorite foods",
            "content": "I like pizza",
            "id": 2}]

@app.get("/")
def root():
    return {"message": "Welcome to my api!"}


@app.get("/posts")
def get_posts():
    return {"data": my_posts}


@app.post("/posts")
def create_posts(post: Post):
    print(post)
    return {"data": post.dict()}