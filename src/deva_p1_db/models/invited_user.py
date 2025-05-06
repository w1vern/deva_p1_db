

from uuid import UUID

from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from deva_p1_db.models.base import Base
from deva_p1_db.models.project import Project
from deva_p1_db.models.user import User


class InvitedUser(Base):
    __tablename__ = "invited_users"

    user_id: Mapped[UUID] = mapped_column(
        ForeignKey("users.id"), primary_key=True)
    project_id: Mapped[UUID] = mapped_column(
        ForeignKey("projects.id"), primary_key=True)

    accepted: Mapped[bool] = mapped_column(default=False)

    user: Mapped[User] = relationship(lazy="selectin", foreign_keys=[user_id])
    project: Mapped[Project] = relationship(lazy="selectin", foreign_keys=[
                                            project_id])
