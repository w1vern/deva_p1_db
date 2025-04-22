


from uuid import UUID, uuid4
from typing import TYPE_CHECKING

from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship



from deva_p1_db.models.base import Base
if TYPE_CHECKING:
    from deva_p1_db.models.file import File


class FileMetadata(Base):
    __tablename__ = "files_metadata"

    id: Mapped[UUID] = mapped_column(primary_key=True, default=uuid4)
    file_id: Mapped[UUID] = mapped_column(ForeignKey("files.id"))
    is_hide: Mapped[bool]
    timecode: Mapped[float]
    text: Mapped[str]

    file: Mapped["File"] = relationship(lazy="selectin", foreign_keys=[file_id])

