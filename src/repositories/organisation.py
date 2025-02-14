from src.database.models import Organisation
from src.repositories.base import BaseRepository
from src.schemas.organisation import SOrganisationsDataBase


class OrganisationRepository(BaseRepository):
    model = Organisation
    model_pydantic_schema = SOrganisationsDataBase
