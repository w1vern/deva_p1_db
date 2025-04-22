

from datetime import datetime
from typing import Optional
from uuid import UUID, uuid4

from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy.sql import func

from deva_p1_db.models.base import Base
from deva_p1_db.models.file_metadata import FileMetadata
from deva_p1_db.models.project import Project
from deva_p1_db.models.task import Task
from deva_p1_db.models.user import User


class File(Base):
    __tablename__ = "files"

    id: Mapped[UUID] = mapped_column(primary_key=True, default=uuid4)
    file_name: Mapped[str]
    file_metadata_id: Mapped[Optional[UUID]] = mapped_column(ForeignKey("files_metadata.id"))
    created_date: Mapped[datetime] = mapped_column(server_default=func.now())
    last_modified_date: Mapped[datetime] = mapped_column(server_default=func.now(), onupdate=func.now())
    file_type: Mapped[str]
    project_id: Mapped[UUID] = mapped_column(ForeignKey("projects.id"))
    user_id: Mapped[UUID] = mapped_column(ForeignKey("users.id"))
    
    task_id: Mapped[UUID] = mapped_column(ForeignKey("tasks.id"))

    user: Mapped[User] = relationship(lazy="selectin", foreign_keys=[user_id])
    project: Mapped[Project] = relationship(lazy="selectin", foreign_keys=[project_id], cascade="all, delete")
    task: Mapped[Task] = relationship(lazy="selectin", foreign_keys=[task_id])
    file_metadata: Mapped[FileMetadata] = relationship(lazy="selectin", foreign_keys=[file_metadata_id])