from typing import Protocol
from uuid import UUID

from src.database.models import Organisation
from src.schemas.organisation import SOrganisationGet, SOrganisationList, SOrganisationID
from src.utils.loger import Logger


class OrganisationRepositoryInterface(Protocol):
    async def get_info_organisation(self, id_: UUID) -> Organisation: ...

    async def get_list_organisation_by_building(self, id_: UUID) -> list[dict]: ...

    async def get_organisations_by_activity(self, child_activity_ids: list[int]) -> list[dict]: ...

    async def get_organisation_by_name(self, name: str) -> int: ...


class ActivityRepositoryInterface(Protocol):
    async def get_all_child_activities(self, parent_id: int) -> list[int]: ...

    async def get_id_parent_activity(self, activity_name: str) -> int: ...


class OrganisationService:
    def __init__(
            self,
            logger: Logger,
            organisation_repository: OrganisationRepositoryInterface,
            activity_repository: ActivityRepositoryInterface
    ) -> None:
        self.logger: Logger = logger
        self.organisation_repository: OrganisationRepositoryInterface = organisation_repository
        self.activity_repository: ActivityRepositoryInterface = activity_repository

    async def get_organisation(self, id_: UUID) -> SOrganisationGet:
        result = await self.organisation_repository.get_info_organisation(id_)

        if not result:
            self.logger.warning("not organisation, invalid id")
            raise ValueError("invalid id")
        self.logger.info("get organisation data")

        return SOrganisationGet.from_orm(result)

    async def get_organisations_by_building(self, id_: UUID) -> list[SOrganisationList]:
        result = await self.organisation_repository.get_list_organisation_by_building(id_)

        if not result:
            self.logger.warning("not building, invalid id")
            raise ValueError("invalid id")
        self.logger.info("get organisations, by building")

        return [SOrganisationList(**row) for row in result]

    async def get_organisation_by_activity(self, activity: str) -> list[SOrganisationList]:
        parent_activity = await self.activity_repository.get_id_parent_activity(activity)

        if not parent_activity:
            self.logger.warning("not activity, invalid id")
            raise ValueError("invalid id")
        self.logger.info("get parent activity")

        child_activity_ids = await self.activity_repository.get_all_child_activities(parent_id=parent_activity)
        self.logger.info("get child activity ids")

        result = await self.organisation_repository.get_organisations_by_activity(child_activity_ids)
        self.logger.info("get organisations by activity")

        return [SOrganisationList(**row) for row in result]

    async def get_organisation_by_name(self, name: str) -> SOrganisationID:
        id_organisation = await self.organisation_repository.get_organisation_by_name(name)

        if not id_organisation:
            self.logger.warning("not organisation, invalid name")
            raise ValueError("invalid name")
        self.logger.info("get id organisation")

        return SOrganisationID(id=id_organisation)
