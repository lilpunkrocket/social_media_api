import psycopg2
from psycopg2.extras import RealDictCursor
from typing import Optional
from fastapi import Body, FastAPI, HTTPException, Response, status, Depends
from pydantic import BaseModel
from . import models
from .database import engine, get_db
from sqlalchemy.orm import Session


models.Base.metadata.create_all(bind=engine)


        
# initializing the main app
app = FastAPI()

# our data schema
class Post(BaseModel):
    title: str
    content: str
    published: bool = True

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
def get_posts(db: Session = Depends(get_db)):
    # cursor.execute("SELECT * FROM posts")
    # posts = cursor.fetchall()
    posts = db.query(models.Post).all()
    return {"data": posts}


# create new post with HTTP POST method
@app.post("/posts", status_code=status.HTTP_201_CREATED)
def create_posts(post: Post, db: Session = Depends(get_db)):
    # cursor.execute("INSERT INTO posts (title, content, published) VALUES (%s, %s, %s) RETURNING *", (post.title, post.content, post.published))
    # conn.commit()
    # return {"data": cursor.fetchone()}
    new_post = models.Post(**post.dict())
    db.add(new_post)
    db.commit()
    db.refresh(new_post)
    return {"data": new_post}


# get detailed view post by id with HTTP GET method
@app.get("/posts/{id}")
def get_post(id: int, db: Session = Depends(get_db)):
    # cursor.execute("SELECT * FROM posts WHERE id = %s", (str(id)))
    # post = cursor.fetchone()

    post = db.query(models.Post).filter(models.Post.id == id).first()

    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, 
                        detail=f'There are no post with id {id}')

    return {"detail post": post}


# delete post by id with HTTP DELETE method
@app.delete('/posts/{id}', status_code=status.HTTP_204_NO_CONTENT)
def delete_post(id: int, db: Session = Depends(get_db)):
    # cursor.execute("DELETE FROM posts WHERE id = %s RETURNING *", (str(id)))
    # post = cursor.fetchone()
    # conn.commit()

    post = db.query(models.Post).filter(models.Post.id == id)

    if post.first() == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, 
                        detail=f'There are no post with id {id}')

    post.delete(synchronize_session=False)
    db.commit()

    return Response(status_code=status.HTTP_204_NO_CONTENT)


# change or update post by HTTP PUT method
@app.put('/posts/{id}')
def update_post(id: int, post: Post, db: Session = Depends(get_db)):
    # cursor.execute("UPDATE posts SET title = %s, content = %s, published = %s WHERE id = %s RETURNING *", (post.title, post.content, post.published, str(id)))
    # conn.commit()
    # updated_post = cursor.fetchone()

    post_query = db.query(models.Post).filter(models.Post.id == id)

    if post_query.first() == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, 
                        detail=f'There are no post with id {id}')

    post_query.update(post.dict(), synchronize_session=False)
    db.commit()

    return {'data': post_query.first()}