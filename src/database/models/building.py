from uuid import UUID

from geoalchemy2 import Geometry
from sqlalchemy import text
from sqlalchemy.orm import Mapped, mapped_column

from src.database.config import Base


class Building(Base):
    __tablename__ = "building"

    id: Mapped[UUID] = mapped_column(primary_key=True, server_default=text('uuid_generate_v4()'))
    address: Mapped[str] = mapped_column(index=True)
    geom: Mapped[Geometry] = mapped_column(Geometry(geometry_type="Point", srid=4326))
