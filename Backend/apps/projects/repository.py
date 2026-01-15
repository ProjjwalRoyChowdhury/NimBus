
# apps/projects/repository.py

from uuid import UUID
from typing import List, Optional

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from apps.projects.models import Project


class ProjectRepository:
    """
    Data access layer for Projects.
    READ-ONLY in this step.
    """

    def __init__(self, session: AsyncSession):
        self.session = session

    async def get_by_id(
        self, *, tenant_id: UUID, project_id: UUID
    ) -> Optional[Project]:
        stmt = (
            select(Project)
            .where(Project.id == project_id)
            .where(Project.tenant_id == tenant_id)
        )
        result = await self.session.execute(stmt)
        return result.scalar_one_or_none()

    async def list_by_tenant(
        self, *, tenant_id: UUID, limit: int = 50, offset: int = 0
    ) -> List[Project]:
        stmt = (
            select(Project)
            .where(Project.tenant_id == tenant_id)
            .limit(limit)
            .offset(offset)
        )
        result = await self.session.execute(stmt)
        return result.scalars().all()
