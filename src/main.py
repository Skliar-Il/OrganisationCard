from fastapi import FastAPI

from src.routers import routers

app = FastAPI(
    title="OrganisationCard",
    version="0.1.0"
)

for router in routers:
    app.include_router(router)
