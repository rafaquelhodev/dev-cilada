from fastapi import FastAPI

from cilada import config
from cilada.adapters import perks as perks_adapter
from cilada.adapters import classifier as classifiers_adapter
from cilada.orm import mapper_registry, start_mappers
from cilada.repository import ClassifierRepositorySqlAlchemy
from cilada.use_cases import CreateClassifier, FindClassifier

app = FastAPI()

engine = config.get_engine()
mapper_registry.metadata.create_all(engine)
start_mappers()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/classifiers/{identifier}")
def read_item(identifier: str):
    repo = ClassifierRepositorySqlAlchemy()

    find_classifier = FindClassifier(identifier, repo)
    classifier = find_classifier.execute()

    return classifiers_adapter.to_view(classifier)


@app.post("/classifiers/")
async def create_item(classifier: classifiers_adapter.BaseClassifier):
    repo = ClassifierRepositorySqlAlchemy()

    perks = perks_adapter.adapt_to_domain(classifier.perks)

    create_classifier = CreateClassifier(perks, classifier.cilada_threshold, repo)
    identifier = create_classifier.execute()

    return identifier