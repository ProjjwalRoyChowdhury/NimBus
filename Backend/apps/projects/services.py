
"""
Business logic for Projects.
Must not import FastAPI, ORM models directly, or request objects.
"""
from apps.projects.repository import ProjectRepository
from apps.projects.schemas import ProjectRead, ProjectListItem

from uuid import UUID
from typing import List

class ProjectNotFoundError(Exception):
    pass

class ProjectService:
    def __init__(self,repository:ProjectRepository):
        self.repository = repository

    async def get_project(self,*,tenant_id : UUID, project_id : UUID) -> ProjectRead:
        project = await self.repository.get_by_id(
            tenant_id = tenant_id,
            project_id = project_id
        )

        if project is None:
            raise ProjectNotFoundError(f"Project {project_id} not found in tenant{tenant_id}")
        
        return ProjectRead.from_orm(project)
    
    async def list_project(self,*,tenant_id : UUID,limit:int = 50,offset:int = 0) -> List[ProjectListItem]:
        list_project = await self.repository.list_by_tenant(
            tenant_id = tenant_id,
            limit = limit,
            offset = offset,
        )

        return [ProjectListItem.from_orm(project) for project in list_project]