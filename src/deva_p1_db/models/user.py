

from uuid import UUID, uuid4

from sqlalchemy.orm import Mapped, mapped_column

from deva_p1_db.models.base import Base


class User(Base):
    __tablename__ = "users"

    id: Mapped[UUID] = mapped_column(primary_key=True, default=uuid4)
    login: Mapped[str] = mapped_column(unique=True)
    hashed_password: Mapped[str]
    secret: Mapped[str]
