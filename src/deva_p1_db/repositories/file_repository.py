from datetime import datetime
from typing import Optional
from uuid import UUID

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from deva_p1_db.models import *


class FileRepository:
    def __init__(self, session: AsyncSession):
        self.session = session

    async def create(self,
                     user_file_name: str,
                     file_type: str,
                     user: User,
                     project: Project,
                     task: Task | None = None, 
                     created_date: datetime | None = None,
                     last_modified_date: datetime | None = None
                     ) -> Optional[File]:
        if created_date is None:
            created_date = datetime.now()
        if last_modified_date is None:
            last_modified_date = datetime.now()
        if task is None:
            task_id = UUID(int=0)
        else:
            task_id = task.id
        file = File(user_file_name=user_file_name,
                    created_date=created_date,
                    last_modified_date=last_modified_date,
                    file_type=file_type,
                    user_id=user.id,
                    project_id=project.id,
                    task_id = task_id)
        self.session.add(file)
        await self.session.flush()
        return await self.get_by_id(file.id)
    
    async def get_by_id(self, file_id: UUID) -> Optional[File]:
        stmt = select(File).where(File.id == file_id)
        return await self.session.scalar(stmt)
    
    async def get_by_project(self, project: Project) -> list[File]:
        stmt = select(File).where(File.project_id == project.id)
        return list((await self.session.scalars(stmt)).all())
    
    async def get_by_user(self, user: User) -> list[File]:
        stmt = select(File).where(File.user_id == user.id)
        return list((await self.session.scalars(stmt)).all())
    
    async def get_by_task(self, task: Task) -> list[File]:
        stmt = select(File).where(File.task_id == task.id)
        return list((await self.session.scalars(stmt)).all())
    
    async def get_by_file_type(self, file_type: str) -> list[File]:
        stmt = select(File).where(File.file_type == file_type)
        return list((await self.session.scalars(stmt)).all())
    
    async def get_by_user_file_name(self, user_file_name: str) -> list[File]:
        stmt = select(File).where(File.user_file_name == user_file_name)
        return list((await self.session.scalars(stmt)).all())
    
    async def delete(self, file: File) -> None:
        await self.session.delete(file)
        await self.session.flush()