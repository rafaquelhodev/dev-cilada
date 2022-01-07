from cilada import config
from cilada.domain import Perk
from cilada.orm import mapper_registry, start_mappers
from cilada.repository import ClassifierRepositorySqlAlchemy
from cilada.use_cases import CreateClassifier

engine = config.get_engine()
mapper_registry.metadata.create_all(engine)
start_mappers()

repo = ClassifierRepositorySqlAlchemy()

tem_cafe = Perk(description="Aqui tem café", cilada_points=15)
casa_do_chefe = Perk(description="Escritório na casa do chefe", cilada_points=15)

create_classifier = CreateClassifier(
    perks={tem_cafe, casa_do_chefe}, cilada_threshold=20, repository=repo
)

identifier = create_classifier.execute()
