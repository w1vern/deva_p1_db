from typing import Optional
from uuid import UUID

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from deva_p1_db.models import File, Project, User


class ProjectRepository:
    def __init__(self, session: AsyncSession):
        self.session = session

    async def create(self,
                     name: str,
                     holder: User,
                     description: str = ""
                     ) -> Optional[Project]:
        projects = await self.get_by_user(holder)
        for project in projects:
            if project.name == name:
                raise Exception("Project with this name already exists")
        project = Project(name=name,
                          description=description,
                          holder_id=holder.id)
        self.session.add(project)
        await self.session.flush()
        return await self.get_by_id(project.id)

    async def get_by_id(self, project_id: UUID) -> Optional[Project]:
        stmt = select(Project).where(Project.id == project_id)
        return await self.session.scalar(stmt)
    
    async def get_by_user(self, user: User) -> list[Project]:
        stmt = select(Project).where(Project.holder_id == user.id)
        return list((await self.session.scalars(stmt)).all())

    async def update(self,
                     project: Project,
                     name: str | None = None,
                     description: str | None = None
                     ) -> None:
        if name is not None:
            project.name = name
        if description is not None:
            project.description = description
        await self.session.flush()

    async def delete(self, project: Project) -> None:
        await self.session.delete(project)
        await self.session.flush()

    async def add_origin_file(self, project: Project, file: File) -> None:
        project.origin_file_id = file.id
        await self.session.flush()

    async def add_summary_file(self, project: Project, file: File) -> None:
        project.summary_id = file.id
        await self.session.flush()

    async def add_transcription_file(self, project: Project, file: File) -> None:
        project.transcription_id = file.id
        await self.session.flush()

    
