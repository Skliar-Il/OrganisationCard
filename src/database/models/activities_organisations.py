from sqlalchemy import ForeignKey, Table, Column, Integer
from sqlalchemy import UUID as SQL_UUID

from src.database.config import Base

organization_activity_association = Table(
    "organisation_activity",
    Base.metadata,
    Column("activity_id", Integer, ForeignKey("activity.id")),
    Column("organisation_id", SQL_UUID, ForeignKey("organisation.id"))
)
