

from datetime import datetime
from uuid import UUID, uuid4

from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from deva_p1_db.models.base import Base
from deva_p1_db.models.file_type import FileType
from deva_p1_db.models.project import Project
from deva_p1_db.models.task import Task


class File(Base):
    __tablename__ = "files"

    id: Mapped[UUID] = mapped_column(primary_key=True, default=uuid4)
    user_file_name: Mapped[str]
    created_date: Mapped[datetime]
    last_modified_date: Mapped[datetime]
    file_type: Mapped[str] = mapped_column()
    project_id: Mapped[UUID] = mapped_column(ForeignKey("projects.id"))
    task_id: Mapped[UUID] = mapped_column(ForeignKey("tasks.id"))


    project: Mapped[Project] = relationship(lazy="selectin", foreign_keys=[project_id])
    task: Mapped[Task] = relationship(lazy="selectin", foreign_keys=[task_id])