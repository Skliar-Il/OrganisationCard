from uuid import UUID

from fastapi import APIRouter, Depends

from src.repositories.organisation import OrganisationRepository
from src.repositories.phone import PhoneRepository
from src.schemas.organisation import SCreateOrganisation
from src.service.organisation import OrganisationService
from src.utils.loger import Logger

router = APIRouter(
    prefix="/organisation",
    tags=["Organisation"],
)


def get_logger() -> Logger:
    return Logger("Organisation")


def get_organisation_service(
        logger: Logger = Depends(get_logger),
        organisation_repository=Depends(OrganisationRepository),
        phone_repository=Depends(PhoneRepository)
) -> OrganisationService:
    return OrganisationService(
        logger,
        organisation_repository,
        phone_repository
    )


# @router.post(
#     "/new",
#     summary="create new organisation",
#     status_code=201,
#     name="new organisation",
#     description="For phone number use format X-XXX-XXX-XX-XX or X-XXX-XXX"
# )
# async def create_organisation(organisation_info: SCreateOrganisation,
#                               service: OrganisationService = Depends(get_organisation_service)) -> None:
#     print(organisation_info.phone)

@router.get(
    "/{id_}",
    summary="get organisation",
    status_code=200,
    name="get organisation",
    description="get organisation by ID"
)
async def get_organisation(id_: UUID) ->
