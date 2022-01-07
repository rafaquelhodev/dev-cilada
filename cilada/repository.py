from abc import ABC
import abc
from typing import Set
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.session import Session

from cilada.domain import CiladaClassifier
from cilada import config


class ClassifierRepository(ABC):
    @abc.abstractmethod
    def add(self, classifier: CiladaClassifier) -> str:
        pass

    @abc.abstractmethod
    def get(self, identifier: str) -> CiladaClassifier:
        pass


class ClassifierRepositoryMemory(ClassifierRepository):
    def __init__(self) -> None:
        self.classifiers: Set[CiladaClassifier] = set()

    def add(self, classifier: CiladaClassifier) -> str:
        self.classifiers.add(classifier)
        return classifier.identifier

    def get(self, identifier: str) -> CiladaClassifier:
        classifier = next(
            (x for x in self.classifiers if x.identifier == identifier), None
        )

        return classifier


DEFAULT_SESSION_FACTORY = sessionmaker(bind=config.get_engine())


class ClassifierRepositorySqlAlchemy(ClassifierRepository):
    def __init__(self, session_factory=DEFAULT_SESSION_FACTORY) -> None:
        self.session = session_factory()  # type: Session

    def add(self, classifier: CiladaClassifier) -> str:
        self.session.add(classifier)
        self.session.commit()
        return classifier.identifier

    def get(self, identifier: str) -> CiladaClassifier:
        classifier = (
            self.session.query(CiladaClassifier).filter_by(identifier=identifier).one()
        )

        return classifier
