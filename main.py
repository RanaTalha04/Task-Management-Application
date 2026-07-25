from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from src.utils.db import Base, engine
from src.tasks.models import TaskModel
from src.user.models import UserModel
from src.tasks.router import task_routes
from src.user.router import user_routes

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Task Management Application")

origins = [
    "http://localhost:5173",              # Local React development
    "https://your-frontend.vercel.app",   # Replace with your Vercel URL
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(task_routes)
app.include_router(user_routes)