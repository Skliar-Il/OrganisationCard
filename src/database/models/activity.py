from sqlalchemy import ForeignKey, CheckConstraint
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.database.config import Base
from src.database.models import organization_activity_association


class Activity(Base):
    __tablename__ = "activity"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(unique=True)
    parent_id: Mapped[int | None] = mapped_column(ForeignKey("activity.id"))
    depth: Mapped[int] = mapped_column(default=0)

    __table_args__ = (
        CheckConstraint('depth >= 0 AND depth <= 2', name='check_depth_range'),
    )

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
