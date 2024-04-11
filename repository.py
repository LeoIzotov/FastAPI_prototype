from database import new_session, TaskOrm
from schemas import STaskAdd, STask
from sqlalchemy import select


class TaskRepository:
    @classmethod
    async def add_one(cls, data: STaskAdd) -> int: # все аннотации через "->" означают тип возвращаемых данных
        async with new_session() as session:
            task_dict = data.model_dump()

            task = TaskOrm(**task_dict)
            session.add(task)
            await session.flush()
            # session.flush() выполнит все нужные действия перед коммитом,\
            # только потом выполнится session.commit()
            await session.commit()
            return task.id

    @classmethod
    async def find_all(cls) -> list[STask]: # все аннотации через "->" означают тип возвращаемых данных
        async with new_session() as session:
            query = select(TaskOrm)
            result = await session.execute(query)
            task_models = result.scalars().all()
            # result.all() || .first() || .one_or_none() || .one() и прочие способы
            task_schemas = [STask.model_validate() for task_model in task_models]
            return task_schemas