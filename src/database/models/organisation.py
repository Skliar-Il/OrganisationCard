from uuid import UUID

from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.database.config import Base
from src.database.models import organization_activity_association


class Organisation(Base):
    __tablename__ = "organisation"

    id: Mapped[UUID] = mapped_column(primary_key=True, server_default="generate_uuid_v4")
    name: Mapped[str] = mapped_column(unique=True)
    building_id: Mapped[UUID] = mapped_column(ForeignKey('building.id', ondelete="CASCADE"))
    phones = relationship(
        "Phone",
        back_populates="organisation",
        uselist=True
    )
    activities = relationship(
        "Activity",
        secondary=organization_activity_association,
        back_populates="organisations"
    )
