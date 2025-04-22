

from datetime import datetime
from typing import TYPE_CHECKING, Optional
from uuid import UUID, uuid4

from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy.sql import func

from deva_p1_db.models.base import Base
from deva_p1_db.models.task import Task
from deva_p1_db.models.user import User

if TYPE_CHECKING:
    from deva_p1_db.models.project import Project


class File(Base):
    __tablename__ = "files"

    id: Mapped[UUID] = mapped_column(primary_key=True, default=uuid4)
    file_name: Mapped[str]
    created_date: Mapped[datetime] = mapped_column(server_default=func.now())
    last_modified_date: Mapped[datetime] = mapped_column(
        server_default=func.now(), onupdate=func.now())
    file_type: Mapped[str]
    user_id: Mapped[UUID] = mapped_column(ForeignKey("users.id"))

    metadata_is_hide: Mapped[Optional[bool]]
    metadata_timecode: Mapped[Optional[float]]
    metadata_text: Mapped[Optional[str]]

    task_id: Mapped[UUID] = mapped_column(ForeignKey("tasks.id",
                                                     use_alter=True,
                                                     name="file_metadata_id",
                                                     deferrable=True,
                                                     initially="DEFERRED"))


    project_id: Mapped[UUID] = mapped_column(ForeignKey("projects.id",
                                                        use_alter=True,
                                                        name="project_id",
                                                        deferrable=True,
                                                        initially="DEFERRED"))

    user: Mapped[User] = relationship(lazy="selectin", foreign_keys=[user_id])
    project: Mapped["Project"] = relationship(lazy="selectin", foreign_keys=[
                                              project_id], cascade="all, delete")
    task: Mapped[Task] = relationship(lazy="selectin", foreign_keys=[task_id])

