from domain.ports.db_provider_port import DbProviderPort
from domain.ports.db_provider_factory_port import DbProviderFactoryPort
from infrastructure.db.db_engines.engine_factory import get_engine
from infrastructure.db.db_executor import DbExecutor
from infrastructure.schema.schema_introspector.sql_server import SQLServerSchemaIntrospector
from infrastructure.schema.schema_normalizer.sql_server import SQLServerSchemaNormalizer
from .db_provider import DbProvider


# Single registry: db_type -> (db_executor_cls, introspector_cls, normalizer_cls)
_DB_REGISTRY = {
    "sqlserver": {
        "db_executor": DbExecutor,
        "introspector": SQLServerSchemaIntrospector,
        "normalizer": SQLServerSchemaNormalizer,
    },
}


class DbProviderFactory(DbProviderFactoryPort):
    def get_db_provider(self, db_type: str, config: dict) -> DbProviderPort:
        entry = _DB_REGISTRY.get(db_type)
        if not entry:
            raise ValueError(f"Unsupported db_type: {db_type}")

        engine = get_engine(db_type, config)

        db_executor = entry["db_executor"](engine)
        introspector = entry["introspector"](engine)
        normalizer = entry["normalizer"]()

        return DbProvider(
            db_executor=db_executor,
            schema_introspector=introspector,
            schema_normalizer=normalizer,
        )

