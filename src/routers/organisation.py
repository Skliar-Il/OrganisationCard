from uuid import UUID

from fastapi import APIRouter, Depends, HTTPException, status

from src.repositories.activity import ActivityRepository
from src.repositories.organisation import OrganisationRepository
from src.schemas.organisation import SOrganisationGet, SOrganisationList, SOrganisationID
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
        activity_repository=Depends(ActivityRepository)
) -> OrganisationService:
    return OrganisationService(
        logger,
        organisation_repository,
        activity_repository
    )


@router.get(
    "/{id_}",
    status_code=200,
    summary="get organisation",
    description="get organisation by ID"
)
async def get_organisation(
        id_: UUID,
        logger: Logger = Depends(get_logger),
        service: OrganisationService = Depends(get_organisation_service)
) -> SOrganisationGet:
    logger.info("func: get_organisation")

    try:
        result = await service.get_organisation(id_)

    except ValueError as e:
        if len(e.args) > 0 and e.args[0] == "invalid id":
            logger.warning("bad request")
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="invalid id, not found")
        else:
            logger.error(f"server error, not now exception: {e}")
            raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)

    logger.info("Success: get_organisation")

    return result


@router.get(
    "/building/{id_}",
    status_code=200,
    summary="organisation in building",
    description="get organisations by building id"
)
async def get_organisations_building(
        id_: UUID,
        logger: Logger = Depends(get_logger),
        service: OrganisationService = Depends(get_organisation_service)
) -> list[SOrganisationList]:
    logger.info("func: get_organisations_building")

    try:
        result = await service.get_organisations_by_building(id_)

    except ValueError as e:
        if len(e.args) > 0 and e.args[0] == "invalid id":
            logger.warning("bad request")
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="invalid id, not found")
        else:
            logger.error(f"server error, not now exception: {e}")
            raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)

    logger.info("Success: get_organisations_building")

    return result


@router.get(
    "/activity/{name}",
    status_code=200,
    summary="organisations by activity",
    description="get organisations by activity"
)
async def get_organisations_by_activity(
        name: str,
        logger: Logger = Depends(get_logger),
        service: OrganisationService = Depends(get_organisation_service)
) -> list[SOrganisationList]:
    logger.info("func: get_organisations_by_activity")

    try:
        result = await service.get_organisation_by_activity(name)

    except ValueError as e:
        if len(e.args) > 0 and e.args[0] == "invalid id":
            logger.warning("bad request")
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="invalid id, not found")
        else:
            logger.error(f"server error, not now exception: {e}")
            raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)

    logger.info("Success: get_organisations_by_activity")
    return result


@router.get(
    "/name/{name}",
    status_code=200,
    summary="organisation by name",
    description="get organisation by name"
)
async def get_organisation_by_name(
        name: str,
        logger: Logger = Depends(get_logger),
        service: OrganisationService = Depends(get_organisation_service)
) -> SOrganisationID:
    logger.info("func: get_organisation_by_name")

    try:
        result = await service.get_organisation_by_name(name)

    except ValueError as e:
        if len(e.args) > 0 and e.args[0] == "invalid name":
            logger.warning("bad request")
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="invalid name, not found")
        else:
            logger.error(f"server error, not now exception: {e}")
            raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)

    logger.info("Success: get_organisation_by_name ")

    return result
