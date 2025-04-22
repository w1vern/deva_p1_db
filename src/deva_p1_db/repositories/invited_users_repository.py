

from typing import Optional

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from deva_p1_db.models import InvitedUser, Project, User


class InvitedUsersRepository:
    def __init__(self, session: AsyncSession):
        self.session = session

    async def create(self,
                     user: User,
                     project: Project,
                     accepted: bool = False,
                     ) -> Optional[InvitedUser]:
        invited_user = InvitedUser(user_id=user.id,
                                   project_id=project.id,
                                   accepted=accepted)
        self.session.add(invited_user)
        await self.session.flush()
        return await self.get_by_id(user, project)

    async def get_by_id(self, user: User, project: Project) -> Optional[InvitedUser]:
        stmt = select(InvitedUser).where(InvitedUser.user_id == user.id).where(
            InvitedUser.project_id == project.id)
        return await self.session.scalar(stmt)

    async def get_by_user(self, user: User) -> list[InvitedUser]:
        stmt = select(InvitedUser).where(
            InvitedUser.user_id == user.id)
        return list((await self.session.scalars(stmt)).all())

    async def get_by_project(self, project: Project) -> list[InvitedUser]:
        stmt = select(InvitedUser).where(
            InvitedUser.project_id == project.id)
        return list((await self.session.scalars(stmt)).all())
