# import psycopg2
# from psycopg2.extras import RealDictCursor


from fastapi import FastAPI
from . import models
from .database import engine
from .routers import post, user, auth

models.Base.metadata.create_all(bind=engine)


        
# initializing the main app
app = FastAPI()


# connecting to database
# while password:=input('Enter password: '):
#     try:
#         conn = psycopg2.connect(host='localhost', database='fastapi', user='postgres', password=password, cursor_factory=RealDictCursor)
#         cursor = conn.cursor()
#         print("Database connection was succesfull")
#         break
#     except Exception as e:
#         print('Connection to database failed')
#         print('Error', e)


# including posts path        
app.include_router(post.router)

# including users path
app.include_router(user.router)

# including user auth
app.include_router(auth.router)

# main page
@app.get("/")
def root():
    return {"message": "Welcome to my api!"}
