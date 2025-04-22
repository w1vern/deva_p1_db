
from uuid import UUID
from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from deva_p1_db.models.base import Base
from deva_p1_db.models.file import File

class ImageSet(Base):
    __tablename__ = "image_sets"
    set_id: Mapped[UUID] = mapped_column(primary_key=True)
    image_id: Mapped[UUID] = mapped_column(ForeignKey("files.id"), primary_key=True)

    image: Mapped[File] = relationship(lazy="selectin", foreign_keys=[image_id])