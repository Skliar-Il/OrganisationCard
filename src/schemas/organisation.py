from uuid import UUID

from pydantic import BaseModel


class SOrganisationsDataBase(BaseModel):
    id: UUID
    name: str
    building_id: UUID

# class SCreateOrganisation(BaseModel):
#     name: str
#     building_id: UUID
#     phones: list[str]
#     activities: list[int]
#
#     @field_validator('phone', mode='before')
#     @classmethod
#     def validate_number(cls, value):
#         pattern = re.compile(
#             r'^(?:\d{1}-\d{3}-\d{3}|\d{1}-\d{3}-\d{3}-\d{2}|'
#             r'\d{1}-\d{3}-\d{3}-\d{2}-\d{2}|\d{1}-\d{3}-\d{3}-\d{2}-\d{2}-\d{2})$'
#         )
#
#         if pattern.match(value):
#             return value
#         else:
#             raise ValueError(f"Invalid format for phone number: {value}")
