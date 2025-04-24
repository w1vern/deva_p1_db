

from datetime import datetime
from typing import TYPE_CHECKING, Optional
from uuid import UUID, uuid4

from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy.sql import func

from deva_p1_db.models.base import Base
from deva_p1_db.models.user import User

if TYPE_CHECKING:
    from deva_p1_db.models.file import File


class Project(Base):
    __tablename__ = "projects"

    id: Mapped[UUID] = mapped_column(primary_key=True, default=uuid4)
    name: Mapped[str]
    description: Mapped[str]
    holder_id: Mapped[UUID] = mapped_column(ForeignKey("users.id"))
    created_date: Mapped[datetime] = mapped_column(server_default=func.now())
    last_modified_date: Mapped[datetime] = mapped_column(server_default=func.now(), onupdate=func.now())

    origin_file_id: Mapped[UUID | None] = mapped_column(ForeignKey("files.id"), default=None, nullable=True)
    transcription_id: Mapped[UUID | None] = mapped_column(ForeignKey("files.id"), default=None, nullable=True)
    summary_id: Mapped[UUID | None] = mapped_column(ForeignKey("files.id"), default=None, nullable=True)
    frames_extract_done: Mapped[bool] = mapped_column(default=False)
    
    holder: Mapped[User] = relationship(lazy="selectin", foreign_keys=[holder_id])

    origin_file: Mapped["File | None"] = relationship(lazy="selectin", foreign_keys=[origin_file_id])
    transcription: Mapped["File | None"] = relationship(lazy="selectin", foreign_keys=[transcription_id])
    summary: Mapped["File | None"] = relationship(lazy="selectin", foreign_keys=[summary_id])



