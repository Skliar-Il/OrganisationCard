from uuid import UUID

from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.database.config import Base


class Phone(Base):
    __tablename__ = "phone"
    id: Mapped[int] = mapped_column(primary_key=True)
    phone: Mapped[str] = mapped_column(unique=True)
    organisation_id: Mapped[UUID] = mapped_column(ForeignKey("organisation.id"))
    organisation = relationship(
        "Organisation",
        back_populates="phones",
        uselist=False
    )
