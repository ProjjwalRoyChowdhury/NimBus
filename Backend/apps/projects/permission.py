
"""
RBAC rules for Projects domain.
"""

from typing import Set

class Project_Permissions:
    _ROLE_PERMISSIONS = {
        "admin": {
            "view_project",
            "list_project",
            "create_project",
            "update_project",
            "archive_project",
        },
        "manager":{
            "view_project",
            "list_project",
            "create_project",
            "update_project",
        },
        "member": {
            "view_project",
            "list_project",
        }
    }

@classmethod
def is_allowed(cls,*,role:str, action:str):
    allowed_actions: set[str] = cls.role._ROLE_PERMISSION.get(role,set())

    return action in allowed_actions
