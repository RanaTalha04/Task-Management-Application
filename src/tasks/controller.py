from src.tasks.dtos import TaskSchema
from sqlalchemy.orm import Session
from src.tasks.models import TaskModel
from fastapi import HTTPException


def create_task(body: TaskSchema, db: Session):

    data = body.model_dump()
    task = TaskModel(
        title=data["title"],
        description=data["description"],
        is_completed=data.get("is_completed", False),
    )

    db.add(task)
    db.commit()
    db.refresh(task)

    return task


def get_task(db: Session):
    tasks = db.query(TaskModel).all()

    return tasks


def get_one_task(task_id: int, db: Session):

    one_task = db.query(TaskModel).get(task_id)
    if not one_task:
        raise HTTPException(
            status_code=404, detail=f"The data with id {task_id} not found"
        )

    return one_task


def update_task(task_id: int, body: TaskSchema, db: Session):
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

    return  task


def delete_task(task_id: int, db: Session):

    task = db.query(TaskModel).get(task_id)

    if not task:
        raise HTTPException(
            status_code=404, detail=f"The data with id {task_id} not found"
        )

    db.delete(task)
    db.commit()

    return None
