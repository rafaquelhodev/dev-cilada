from sqlalchemy import (
    Table,
    MetaData,
    Column,
    Integer,
    String,
    ForeignKey,
)
from sqlalchemy.orm import relationship, registry
from sqlalchemy.sql.sqltypes import Boolean

from cilada import domain


metadata = MetaData()
mapper_registry = registry()

perks = Table(
    "perks",
    mapper_registry.metadata,
    Column("id", Integer, primary_key=True, autoincrement=True),
    Column("description", String(255), nullable=False),
    Column("cilada_points", Integer, nullable=False),
    Column("identifier", String, nullable=False),
    Column("classifier_id", Integer, ForeignKey("classifiers.id")),
)

classifiers = Table(
    "classifiers",
    mapper_registry.metadata,
    Column("id", Integer, primary_key=True, autoincrement=True),
    Column("cilada_threshold", Integer, nullable=False),
    Column("identifier", String, nullable=False),
)


def start_mappers():
    perks_mapper = mapper_registry.map_imperatively(domain.Perk, perks)
    mapper_registry.map_imperatively(
        domain.CiladaClassifier,
        classifiers,
        properties={
            "perks": relationship(
                perks_mapper,
                collection_class=set,
            )
        },
    )
