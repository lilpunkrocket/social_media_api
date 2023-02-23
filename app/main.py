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
        

# main page
@app.get("/")
def root():
    return {"message": "Welcome to my api!"}


# get all posts with HTTP GET method
@app.get("/posts")
def get_posts():
    cursor.execute("SELECT * FROM post")
    return {"data": cursor.fetchall()}


# create new post with HTTP POST method
@app.post("/posts", status_code=status.HTTP_201_CREATED)
def create_posts(post: Post):
    cursor.execute("INSERT INTO post (title, content, published) VALUES (%s, %s, %s) RETURNING *", (post.title, post.content, post.published))
    conn.commit()
    return {"data": cursor.fetchone()}


# get detailed view post by id with HTTP GET method
@app.get("/posts/{id}")
def get_post(id: int):
    cursor.execute("SELECT * FROM post WHERE id = %s", (str(id)))
    post = cursor.fetchone()
    if post == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, 
                        detail=f'There are no post with id {id}')
    return {"detail post": post}


# delete post by id with HTTP DELETE method
@app.delete('/posts/{id}', status_code=status.HTTP_204_NO_CONTENT)
def delete_post(id: int):
    cursor.execute("DELETE FROM post WHERE id = %s RETURNING *", (str(id)))
    post = cursor.fetchone()
    conn.commit()
    if post == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, 
                        detail=f'There are no post with id {id}')
    return Response(status_code=status.HTTP_204_NO_CONTENT)


# change or update post by HTTP PUT method
@app.put('/posts/{id}')
def update_post(id: int, post: Post):
    cursor.execute("UPDATE post SET title = %s, content = %s, published = %s WHERE id = %s RETURNING *", (post.title, post.content, post.published, str(id)))
    conn.commit()
    updated_post = cursor.fetchone()
    if updated_post == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, 
                        detail=f'There are no post with id {id}')
    return {'data': updated_post}