




from uuid import UUID, uuid4

from sqlalchemy.orm import Mapped, mapped_column

from deva_p1_db.models.base import Base


class FileType(Base):
    __tablename__ = "file_types"
    id: Mapped[UUID] = mapped_column(primary_key=True, default=uuid4)
    name: Mapped[str] = mapped_column(unique=True)