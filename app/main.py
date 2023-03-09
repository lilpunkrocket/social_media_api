from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from . import models
from .database import engine
from .config import settings
from .routers import post, user, auth, vote

# models.Base.metadata.create_all(bind=engine)
        
# initializing the main app
app = FastAPI()

origins = ['*']

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# including posts path        
app.include_router(post.router)

# including users path
app.include_router(user.router)

# including user auth
app.include_router(auth.router)

# including voting
app.include_router(vote.router)

# main page
@app.get("/")
def root():
    return {"message": "Welcome to my api!"}
