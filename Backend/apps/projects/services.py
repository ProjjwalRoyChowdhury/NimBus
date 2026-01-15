
"""
Business logic for Projects.
Must not import FastAPI, ORM models directly, or request objects.
"""
from app.projects.repository import ProjectRepository
from apps.projects.models import Project

from uuid import UUID
from typing import List

class ProjectNotFoundError():
    pass

class ProjectServices:
    def __init__(self,repository:ProjectRepository):
        self.repository = repository

    async def get_project(
            self,*,tenant_id = UUID, project_id = UUID
    ) -> Project:
        project = await self.repository.get_by_id(
            tenant_id = tenant_id,
            project_id = project_id
        )

        if project is None:
            raise ProjectNotFoundError(
                f"Project{project_id} is not found in tenant{tenant_id}"
            )
        return project
    
    
    async def list_project(self,*,tenant_id = UUID,limit:int = 50,offset:int=0)->list[Project]:
        
        return list_project