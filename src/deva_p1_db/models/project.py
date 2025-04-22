

from datetime import datetime
from uuid import UUID, uuid4

from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from deva_p1_db.models.user import User
from deva_p1_db.models.base import Base

class Project(Base):
    __tablename__ = "projects"

    id: Mapped[UUID] = mapped_column(primary_key=True, default=uuid4)
    name: Mapped[str]
    description: Mapped[str]
    holder_id: Mapped[UUID] = mapped_column(ForeignKey("users.id"))
    created_date: Mapped[datetime]
    last_modified_date: Mapped[datetime]


    holder: Mapped[User] = relationship(lazy="selectin", foreign_keys=[holder_id]) 
