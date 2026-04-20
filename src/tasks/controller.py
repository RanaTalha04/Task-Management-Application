from src.tasks.dtos import TaskSchema
from sqlalchemy.orm import session
from src.tasks.models import TaskModel
from fastapi import HTTPException
from typing import List


def create_task(body: List[TaskSchema], db: session):

    new_tasks = []

    for item in body:
        data = item.model_dump()
        task = TaskModel(
            title=data["title"],
            description=data["description"],
            is_completed=data.get("is_completed", False),
        )

        db.add(task)
        new_tasks.append(task)
    db.commit()

    for task in new_tasks:
        db.refresh(task)

    return {"status": "Tasks added successfully", "data": new_tasks}


def get_task(db: session):
    tasks = db.query(TaskModel).all()

    return {"status": "Data fetched successfully", "data": tasks}


def get_one_task(task_id: int, db: session):

    one_task = db.query(TaskModel).get(task_id)
    if not one_task:
        raise HTTPException(
            status_code=404, detail=f"The data with id {task_id} not found"
        )

    return {"status": "Task fetched successfully", "data": one_task}


def update_task(task_id: int, body: TaskSchema, db: session):
    task = db.query(TaskModel).get(task_id)

    if not task:
        raise HTTPException(
            status_code=404, detail=f"The data with id {task_id} not found"
        )

    task.title = body.title
    task.description = body.description
    task.is_completed = body.is_completed

    db.add(task)
    db.commit()
    db.refresh(task)

    return {"status": "Task updated successfully", "data": f"updated task data {task}"}


def delete_task(task_id: int, db: session):

    task = db.query(TaskModel).get(task_id)

    if not task:
        raise HTTPException(
            status_code=404, detail=f"The data with id {task_id} not found"
        )
    
    db.delete(task)
    db.commit()

    return {"status": "Task deleted successfully", "data": f"Deleted task {task}"}
