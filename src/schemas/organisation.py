from uuid import UUID

from pydantic import BaseModel

from src.database.models import Organisation


class SOrganisationsDataBase(BaseModel):
    id: UUID
    name: str
    building_id: UUID


class SOrganisationGet(BaseModel):
    id: UUID
    name: str
    address: str
    phones: list[str]
    activities: list[str]

    @classmethod
    def from_orm(cls, organisation: Organisation):
        return cls(
            id=organisation.id,
            name=organisation.name,
            address=organisation.building.address,
            phones=[phone.phone for phone in organisation.phones],
            activities=[activity.name for activity in organisation.activities]
        )


class SOrganisationList(BaseModel):
    id: UUID
    name: str


class SOrganisationID(BaseModel):
    id: UUID
