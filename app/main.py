import psycopg2
from psycopg2.extras import RealDictCursor
from typing import Optional
from fastapi import Body, FastAPI, HTTPException, Response, status
from pydantic import BaseModel

# initializing the main app
app = FastAPI()

# our data schema
class Post(BaseModel):
    title: str
    content: str
    published: bool = True
    rating: Optional[int] = None

while password:=input('Enter password: '):
    try:
        conn = psycopg2.connect(host='localhost', database='fastapi', user='postgres', password=password, cursor_factory=RealDictCursor)
        cursor = conn.cursor()
        print("Database connection was succesfull")
        break
    except Exception as e:
        print('Connection to database failed')
        print('Error', e)


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
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, 
                        detail=f'There are no post with id {id}')

def find_index(id):
    for i, v in enumerate(posts):
        if v.get('id') == id:
            return i
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, 
                        detail=f'There are no post with id {id}')

@app.get("/")
def root():
    return {"message": "Welcome to my api!"}


@app.get("/posts")
def get_posts():
    return {"data": posts}



@app.post("/posts", status_code=status.HTTP_201_CREATED)
def create_posts(post: Post):
    dict_post = post.dict()
    dict_post['id'] = posts[-1].get('id', 0) + 1
    posts.append(dict_post)
    return {"data": dict_post}


@app.get("/posts/{id}")
def get_post(id: int, response: Response):
    return {"detail post": find_post(id)}


@app.delete('/posts/{id}', status_code=status.HTTP_204_NO_CONTENT)
def delete_post(id: int):
    posts.pop(find_index(id))
    return Response(status_code=status.HTTP_204_NO_CONTENT)


@app.put('/posts/{id}')
def update_post(id: int, post: Post):
    index = find_index(id)
    posts[index] = post.dict()
    posts[index]['id'] = id
    return {'data': find_post(id)}