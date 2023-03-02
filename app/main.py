from fastapi import FastAPI
from . import models
from .database import engine
from .config import settings
from .routers import post, user, auth

models.Base.metadata.create_all(bind=engine)
        
# initializing the main app
app = FastAPI()

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
