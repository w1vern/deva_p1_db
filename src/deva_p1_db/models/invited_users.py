

from datetime import datetime
from uuid import UUID

from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

from deva_p1_db.models.base import Base


class InvitedUsers(Base):
    __tablename__ = "invited_users"

    user_id : Mapped[UUID] = mapped_column(ForeignKey("users.id"), primary_key=True)
    project_id : Mapped[UUID] = mapped_column(ForeignKey("projects.id"), primary_key=True)

    accepted: Mapped[bool]
    rights_level: Mapped[int]

