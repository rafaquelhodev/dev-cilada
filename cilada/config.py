import os
from sqlalchemy import create_engine


def get_postgres_uri():
    host = os.environ.get("DB_HOST", "localhost")
    port = os.environ.get("DB_PORT", "5432")
    password = os.environ.get("DB_PASSWORD", "1234")
    user, db_name = "postgres", "cilada"
    return f"postgresql://{user}:{password}@{host}:{port}/{db_name}"


def get_engine(get_db_uri=get_postgres_uri):
    return create_engine(
        get_db_uri(),
        isolation_level="REPEATABLE READ",
    )
