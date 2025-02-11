from fastapi import APIRouter

from src.service.organisation import OrganisationService
from src.utils.loger import Logger

router = APIRouter(
    prefix="/organisation",
    tags=["Create", "Info"],
)

logger = Logger("Organisation")
service = OrganisationService(logger)