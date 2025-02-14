from src.repositories.base import BaseRepository
from src.utils.loger import Logger


class OrganisationService:
    def __init__(
            self,
            logger: Logger,
            organisation_repository: BaseRepository,
            phone_repository: BaseRepository
    ) -> None:
        self.logger = logger
        self.organisation_repository = organisation_repository
        self.phone_repository = phone_repository

    async def get_organisation(self, ): ...

    # async def create_organisation(self, organisation_info: SCreateOrganisation):
    #     organisation_id = await self.organisation_repository.create(
    #         **organisation_info.model_dump(exclude={"phone", "activities"})
    #     )
    #     phones_data = SPhonesCreate(phones=organisation_info.phones, organisation_id=organisation_id)
    #
