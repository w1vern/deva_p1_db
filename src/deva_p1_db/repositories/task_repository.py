

from typing import Optional
from uuid import UUID

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from deva_p1_db.models import Project, Task, User


class TaskRepository:
    def __init__(self, session: AsyncSession):
        self.session = session

    async def create(self,
                     user: User,
                     project: Project,
                     task_type: str,
                     prompt: str = "",
                     origin_task: Task | None = None
                     ) -> Task | None:
        task = Task(task_type=task_type,
                    project_id=project.id,
                    user_id=user.id,
                    prompt=prompt,
                    origin_task_id=origin_task.id if origin_task else None)
        self.session.add(task)
        await self.session.flush()
        return await self.get_by_id(task.id)

    async def get_by_id(self, task_id: UUID) -> Task | None:
        stmt = select(Task).where(Task.id == task_id)
        return await self.session.scalar(stmt)

    async def get_by_project(self, project: Project) -> list[Task]:
        stmt = select(Task).where(Task.project_id == project.id)
        return list((await self.session.scalars(stmt)).all())

    async def get_by_user(self, user: User) -> list[Task]:
        stmt = select(Task).where(Task.user_id == user.id)
        return list((await self.session.scalars(stmt)).all())

    async def get_by_project_and_user(self, user: User, project: Project) -> list[Task]:
        stmt = select(Task).where(Task.project_id ==
                                  project.id).where(Task.user_id == user.id)
        return list((await self.session.scalars(stmt)).all())

    async def get_by_origin_task(self, task: Task) -> list[Task]:
        stmt = select(Task).where(Task.origin_task_id == task.id)
        return list((await self.session.scalars(stmt)).all())
    
    async def task_done(self, task: Task):
        task.done = True
        await self.session.flush()
