from sqlalchemy import create_engine

from .scheme import Base


def setup_database(drop_all, db_uri):
    engine = create_engine(db_uri)
    if drop_all:
        Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)
