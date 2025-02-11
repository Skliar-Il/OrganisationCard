from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.database.config import Base
from src.database.models import organization_activity_association


class Activity(Base):
    __tablename__ = "activity"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(unique=True)
    parent_id: Mapped[int] = mapped_column(ForeignKey("activity.id"), nullable=True)
    depth: Mapped[int] = mapped_column(default=0)
    parent = relationship(
        "Activity",
        remote_side=[id],
        backref="children"
    )
    organisations = relationship(
        "Organisation",
        secondary=organization_activity_association,
        back_populates="activities"
    )
