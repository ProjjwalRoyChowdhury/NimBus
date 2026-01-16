
"""
ORM models for the Projects domain.
NO business logic allowed in this file.
"""

from datetime import datetime
from uuid import UUID
from sqlalchemy import ForeignKey, column, String, Text, DateTime
from sqlalchemy.dialects.postgresql import UUID as PG_UUID
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class Project(Base):
    __tablename__ = "projects"

    id = column(PG_UUID(as_uuid=True), primary_key = True)
    tenant_id = column(
        PG_UUID(as_uuid=True), 
        ForeignKey("tenants.id", ondelete = "RESTRICT"),
        nullable = False,
        index = True
        )
    name = column(String(255), nullable = False)
    description = column(Text, nullabl = True)
    status = column(String(255), nullable = False)

    created_by = column(
        PG_UUID(as_uuid=True),
        ForeignKey("users.id", ondelete= "RESTRICT"),
        nullable = False,
    )

    created_at = column(DateTime(timezone=True),nullable = False)
    updated_at = column(DateTime(timezone = True), nullable = False)