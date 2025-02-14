from src.database.models import Phone
from src.repositories.base import BaseRepository
from src.schemas.phone import SPhoneDataBase


class PhoneRepository(BaseRepository):
    model = Phone
    model_pydantic_schema = SPhoneDataBase

    # async def create_phones(self, data: SPhonesCreate) -> None:
    #     async with async_session_factory() as session:
    #         for phone in data.phones:
    #             query = insert(self.model).values(phone=phone, organisation_id=data.organisation_id)
    #             await session.execute(query)
    #
    #         await session.commit()
