from sqlalchemy import select
from sqlalchemy.orm import aliased

from src.database.config import async_session_factory
from src.database.models import Activity


class ActivityRepository:
    model = Activity

    async def get_all_child_activities(self, parent_id: int) -> list[int]:
        async with async_session_factory() as session:
            ActivityAlias = aliased(self.model)

            recursive_cte = select(ActivityAlias.id).where(ActivityAlias.id == parent_id).cte(recursive=True)

            recursive_part = select(ActivityAlias.id).where(ActivityAlias.parent_id == recursive_cte.c.id)

            recursive_cte = recursive_cte.union_all(recursive_part)

            final_query = select(recursive_cte.c.id)
            result = await session.execute(final_query)
            activity_ids = result.scalars().all()
            return activity_ids

    async def get_id_parent_activity(self, activity_name: str):
        async with async_session_factory() as session:
            parent_activity_query = select(self.model.id).where(self.model.name == activity_name)
            parent_activity_result = await session.execute(parent_activity_query)
            parent_activity = parent_activity_result.scalar()

            return parent_activity
