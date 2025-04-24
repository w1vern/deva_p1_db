from typing import Optional
from uuid import UUID

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from deva_p1_db.enums.file_type import FileCategory, resolve_file_type
from deva_p1_db.models import File, Project, Task, User


class FileRepository:
    def __init__(self, session: AsyncSession):
        self.session = session

    async def create(self,
                     user_file_name: str,
                     file_type: str,
                     file_size: int,
                     user: User,
                     project: Project,
                     task: Task | None = None,
                     metadata_is_hide: bool | None = None,
                     metadata_timecode: float | None = None,
                     metadata_text: str | None = None
                     ) -> File | None:
        if task is None:
            task_id = UUID(int=0)
        else:
            task_id = task.id
        file = File(user_file_name=user_file_name,
                    file_type=file_type,
                    file_size=file_size,
                    user_id=user.id,
                    project_id=project.id,
                    task_id=task_id,
                    metadata_is_hide=metadata_is_hide,
                    metadata_timecode=metadata_timecode,
                    metadata_text=metadata_text)
        self.session.add(file)
        await self.session.flush()
        return await self.get_by_id(file.id)

    async def get_by_id(self, file_id: UUID) -> File | None:
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
        stmt = select(File).where(File.file_name == user_file_name)
        return list((await self.session.scalars(stmt)).all())

    async def delete(self, file: File) -> None:
        await self.session.delete(file)
        await self.session.flush()

    async def get_by_project_and_category(self, project: Project, category: str) -> list[File]:
        stmt = select(File).where(File.project_id == project.id)
        project_files = list((await self.session.scalars(stmt)).all())
        return [file for file in project_files if resolve_file_type(file.file_type)]

    async def get_active_images(self, project: Project) -> list[File]:
        _ = await self.get_by_project_and_category(project, FileCategory.image.value)
        return [file for file in _ if file.metadata_is_hide == True]

    async def update_metadata(self,
                              file: File,
                              is_hide: bool | None = None,
                              timecode: float | None = None,
                              text: str | None = None
                              ) -> None:
        if is_hide is not None:
            file.metadata_is_hide = is_hide
        if timecode is not None:
            file.metadata_timecode = timecode
        if text is not None:
            file.metadata_text = text
        await self.session.flush()
