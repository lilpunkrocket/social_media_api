from typing import Optional
from fastapi import Body, FastAPI
from pydantic import BaseModel

# initializing the main app
app = FastAPI()

# our data schema
class Post(BaseModel):
    title: str
    content: str
    published: bool = True
    rating: Optional[int] = None


posts = [{"title": "top beaches on Florida",
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
    return {"data": posts}


@app.post("/posts")
def create_posts(post: Post):
    print(post)
    return {"data": post.dict()}