from typing import Annotated

from fastapi import APIRouter, Depends

from repository import TaskRepository
from schemas import STaskAdd, STask, STaskId

router = APIRouter(
    prefix="/tasks",
    tags=["Таски"],
)


@router.post("")
async def add_task(
        task: Annotated[STaskAdd, Depends()],
) -> STaskId: # все аннотации через "->" означают тип возвращаемых данных
    task_id = await TaskRepository.add_one(task)
    return {"ok": True, "task_id": task_id}
    #здесь ругается питон - НЕ FastAPI!!! Фастапи умный, он проверит может ли он сконвертировать в нужный тип данных


@router.get("/tasks")
async def get_tasks() -> list[STask]: # все аннотации через "->" означают тип возвращаемых данных
    tasks = await TaskRepository.find_all()
    return {"data": tasks}
