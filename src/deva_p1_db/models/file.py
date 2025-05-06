

from datetime import datetime
from typing import TYPE_CHECKING
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
    file_size: Mapped[int]
    user_id: Mapped[UUID] = mapped_column(ForeignKey("users.id"))

    metadata_is_hide: Mapped[bool | None]
    metadata_timecode: Mapped[float | None]
    metadata_text: Mapped[str | None]

    task_id: Mapped[UUID | None] = mapped_column(ForeignKey("tasks.id",
                                                            use_alter=True,
                                                            name="file_metadata_id",
                                                            deferrable=True,
                                                            initially="DEFERRED"),
                                                 nullable=True)

    project_id: Mapped[UUID] = mapped_column(ForeignKey("projects.id",
                                                        use_alter=True,
                                                        name="project_id",
                                                        deferrable=True,
                                                        initially="DEFERRED"))

    user: Mapped[User] = relationship(lazy="selectin", foreign_keys=[user_id])
    project: Mapped["Project"] = relationship(lazy="selectin", foreign_keys=[
                                              project_id])
    task: Mapped[Task | None] = relationship(
        lazy="selectin", foreign_keys=[task_id])

    @property
    def minio_name(self) -> str:
        return str(self.id)
