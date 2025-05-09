

from secrets import token_urlsafe
from typing import Optional
from uuid import UUID

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from werkzeug.security import check_password_hash, generate_password_hash

from deva_p1_db.models import User


class UserRepository:
    def __init__(self, session: AsyncSession):
        self.session = session

    async def create(self, login: str, password: str) -> User | None:
        user = User(login=login,
                    hashed_password=generate_password_hash(password),
                    secret=token_urlsafe(32))
        self.session.add(user)
        await self.session.flush()
        return await self.get_by_id(user.id)

    async def get_by_id(self, user_id: UUID) -> User | None:
        stmt = select(User).where(User.id == user_id)
        return await self.session.scalar(stmt)
    
    async def get_by_login(self, login: str) -> Optional[User]:
        stmt = select(User).where(User.login == login)
        return await self.session.scalar(stmt)

    async def get_by_auth(self, login: str, password: str) -> User | None:
        stmt = select(User).where(User.login == login).limit(1)
        user = await self.session.scalar(stmt)
        if user is None:
            return None
        if not check_password_hash(user.hashed_password, password):
            return None
        return user
    
    async def update_credentials(self, user: User, login: str | None = None, password: str | None = None) -> None:
        if login is not None:
            user.login = login
        if password is not None:
            user.hashed_password = generate_password_hash(password)
        await self.session.flush()

    async def update_secret(self, user: User) -> None:
        user.secret = token_urlsafe(32)
        await self.session.flush()
