from fastapi import APIRouter, Depends
from src.tasks import controller
from src.tasks.dtos import TaskSchema
from src.utils.db import get_db
from typing import List


task_routes = APIRouter(prefix="/tasks")


@task_routes.post("/create")
def create_task(body: List[TaskSchema], db = Depends(get_db)):
    
    return controller.create_task(body, db)


@task_routes.get("/fetch")
def get_task(db = Depends(get_db)):
    
    return controller.get_task(db)


@task_routes.get("/one_task/{task_id}")
def get_one_task(task_id:int, db = Depends(get_db)):
    
    return controller.get_one_task(task_id, db)

@task_routes.put("/update/{task_id}")
def update_task(task_id: int, body: TaskSchema, db = Depends(get_db)):
    
    return controller.update_task(task_id, body, db)

@task_routes.delete("/delete/{task_id}")
def delete_task(task_id: int, db = Depends(get_db)):
    
    return controller.delete_task(task_id, db)