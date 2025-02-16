import asyncio

from sqlalchemy import insert
from sqlalchemy.ext.asyncio import AsyncSession

from seeds.exemple_data import buildings, activities, organisations, phones, organisations_activities
from src.database.config import async_session_factory
from src.database.models import organization_activity_association


async def seed_database(session: AsyncSession):
    session.add_all(buildings)

    session.add_all(activities)

    session.add_all(organisations)

    session.add_all(phones)

    await session.flush()

    for org_activity in organisations_activities:
        stmt = insert(organization_activity_association).values(
            activity_id=org_activity["activity_id"],
            organisation_id=org_activity["organisation_id"]
        )
        await session.execute(stmt)

    await session.commit()


async def gen_seed():
    async with async_session_factory() as session:
        await seed_database(session)


if __name__ == "__main__":
    asyncio.run(gen_seed())
