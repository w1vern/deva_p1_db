

from uuid import UUID, uuid4

from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from deva_p1_db.models.base import Base
from deva_p1_db.models.project import Project
from deva_p1_db.models.user import User


class Task(Base):
    __tablename__ = "tasks"

    id: Mapped[UUID] = mapped_column(primary_key=True, default=uuid4)
    done: Mapped[bool] = mapped_column(default=False)
    task_type: Mapped[str]
    prompt: Mapped[str]
    subtask_count: Mapped[int]

    project_id: Mapped[UUID] = mapped_column(ForeignKey("projects.id"))
    user_id: Mapped[UUID] = mapped_column(ForeignKey("users.id"))
    origin_task_id: Mapped[UUID | None
                           ] = mapped_column(ForeignKey("tasks.id"), nullable=True)

    project: Mapped[Project] = relationship(lazy="selectin", foreign_keys=[
                                            project_id])
    user: Mapped[User] = relationship(lazy="selectin", foreign_keys=[user_id])
    origin_task: Mapped["Task | None"] = relationship(
        lazy="joined", foreign_keys=[origin_task_id], remote_side="Task.id")
