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

def find_post(id):
    for post in posts:
        if post.get("id", -1) == id:
            return post
    raise ValueError

@app.get("/")
def root():
    return {"message": "Welcome to my api!"}


@app.get("/posts")
def get_posts():
    return {"data": posts}


@app.post("/posts")
def create_posts(post: Post):
    post_dict = post.dict()
    post_dict['id'] = posts[-1].get('id', 0) + 1
    posts.append(post_dict)
    return {"data": post.dict()}


@app.get("/posts/{id}")
def get_post(id: int):
    try:
        return {"detail post": find_post(id)}
    except ValueError:
        return {"Error,": "There are no post with this id"}