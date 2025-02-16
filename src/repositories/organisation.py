from uuid import UUID

from sqlalchemy import select
from sqlalchemy.orm import selectinload

from src.database.config import async_session_factory
from src.database.models import Organisation, organization_activity_association
from src.repositories.base import BaseRepository
from src.schemas.organisation import SOrganisationsDataBase


class OrganisationRepository(BaseRepository):
    model = Organisation
    model_pydantic_schema = SOrganisationsDataBase

    async def get_info_organisation(self, id_: UUID) -> Organisation:
        async with async_session_factory() as session:
            query = (
                select(self.model)
                .options(selectinload(self.model.phones))
                .options(selectinload(self.model.activities))
                .options(selectinload(self.model.building))
                .where(self.model.id == id_)
            )
            result_no_format = await session.execute(query)
            result = result_no_format.scalars().unique().one_or_none()
            return result

    async def get_list_organisation_by_building(self, id_: UUID) -> list[dict]:
        async with async_session_factory() as session:
            query = select(self.model.id, self.model.name).where(self.model.building_id == id_)
            result = await session.execute(query)
            return result.mappings().all()

    async def get_organisations_by_activity(self, child_activity_ids: list[int]) -> list[dict]:
        async with async_session_factory() as session:
            organisations_query = (
                select(self.model.id, self.model.name)
                .join(organization_activity_association,
                      Organisation.id == organization_activity_association.c.organisation_id)
                .where(organization_activity_association.c.activity_id.in_(child_activity_ids))
                .distinct()
            )
            result = await session.execute(organisations_query)
            return result.mappings().all()

    async def get_organisation_by_name(self, name: str) -> int:
        async with async_session_factory() as session:
            query = select(self.model.id).where(self.model.name == name)
            result = await session.execute(query)

            return result.scalar()
