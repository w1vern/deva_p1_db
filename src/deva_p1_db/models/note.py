

from uuid import UUID, uuid4

from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from deva_p1_db.models.base import Base
from deva_p1_db.models.file import File


class Note(Base):
    __tablename__ = "notes"

    id: Mapped[UUID] = mapped_column(primary_key=True, default=uuid4)
    text: Mapped[str]
    start_time_code: Mapped[float]
    end_time_code: Mapped[float]
    file_id: Mapped[UUID] = mapped_column(ForeignKey("files.id"))
    
    file: Mapped[File] = relationship(lazy="selectin", foreign_keys=[file_id])