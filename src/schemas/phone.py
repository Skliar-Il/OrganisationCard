from uuid import UUID

from pydantic import BaseModel


class SPhoneDataBase(BaseModel):
    id: int
    phone: str
    organisation_id: UUID


class SPhonesCreate(BaseModel):
    phones: list[str]
    organisation_id: UUID
