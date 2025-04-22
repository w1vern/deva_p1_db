

from datetime import datetime
from uuid import UUID, uuid4

from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from deva_p1_db.models.base import Base
from deva_p1_db.models.project import Project
from deva_p1_db.models.task import Task
from deva_p1_db.models.user import User


class File(Base):
    __tablename__ = "files"

    id: Mapped[UUID] = mapped_column(primary_key=True, default=uuid4)
    file_name: Mapped[str]
    created_date: Mapped[datetime]
    last_modified_date: Mapped[datetime]
    file_type: Mapped[str]
    project_id: Mapped[UUID] = mapped_column(ForeignKey("projects.id"))
    user_id: Mapped[UUID] = mapped_column(ForeignKey("users.id"))
    
    task_id: Mapped[UUID] = mapped_column(
        ForeignKey("tasks.id", use_alter=True, name="fk_file_task", deferrable=True, initially="DEFERRED"),
        nullable=True
    )

    user: Mapped[User] = relationship(lazy="selectin", foreign_keys=[user_id])
    project: Mapped["Project"] = relationship(lazy="selectin", foreign_keys=[project_id])
    task: Mapped[Task] = relationship(lazy="selectin", foreign_keys=[task_id])