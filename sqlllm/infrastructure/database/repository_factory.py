from __future__ import annotations

from typing import TYPE_CHECKING

from ...domain.entities.database import DatabaseType
from .mysql_repository import MySQLRepository
from .postgresql_repository import PostgreSQLRepository

if TYPE_CHECKING:
    from ...domain.interfaces.database_repository import DatabaseRepository


class DatabaseRepositoryFactory:
    _repositories: dict[DatabaseType, type[DatabaseRepository]] = {
        DatabaseType.MYSQL: MySQLRepository,
        DatabaseType.POSTGRESQL: PostgreSQLRepository,
    }

    @classmethod
    def create(cls, database_type: DatabaseType) -> DatabaseRepository:
        repository_class = cls._repositories.get(database_type)
        if not repository_class:
            raise ValueError(f"Unsupported database type: {database_type}")
        return repository_class()
