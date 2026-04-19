from src.tasks.dtos import TaskSchema
from sqlalchemy.orm import session
from src.tasks.models import TaskModel
from fastapi import HTTPException

def create_task(body: TaskSchema, db: session):

    data = body.model_dump()
    new_task = TaskModel(title = data["title"], description = data["description"], is_completed = data["is_completed"])

    db.add(new_task)
    db.commit()
    db.refresh(new_task)

    return {"Status": "Tasks created successfully", "data": new_task}



def get_task(db: session):
    tasks = db.query(TaskModel).all()

    return {
        "status": "Data fetched successfully",
        "data": tasks
    } 


def get_one_task(task_id:int, db: session):
    
    one_task = db.query(TaskModel).get(task_id)
    if not one_task:
        raise HTTPException(status_code = 404, detail = f"The data with id {task_id} not found")
    
    return {
        "status": "Task fetched successfully",
        "data": one_task
    }