from .db import DB
from .engines.factory import get_Engine
from ..schema_manager.schema_introspector.factory import get_schema_inspector
from ..schema_manager.schema_normalizer.factory import get_schema_normalizer


def get_database(dbType: str):
    engine=get_Engine(dbType)
    inspector = get_schema_inspector(dbType,engine)
    normalizer = get_schema_normalizer(dbType)
    return DB(engine, inspector, normalizer)

    
