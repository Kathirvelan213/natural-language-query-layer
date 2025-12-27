from typing import Protocol
from sqlalchemy.engine import Engine

class DB_Engine(Protocol): 
    engine: Engine
    