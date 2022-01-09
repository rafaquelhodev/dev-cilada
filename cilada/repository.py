from abc import ABC
import abc
from typing import Set
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.session import Session

from cilada.domain import CiladaClassifier, Perk
from cilada import config


class ClassifierRepository(ABC):
    @abc.abstractmethod
    def add(self, classifier: CiladaClassifier) -> str:
        pass

    @abc.abstractmethod
    def get(self, identifier: str) -> CiladaClassifier:
        pass

    @abc.abstractmethod
    def get_perks(self, identifier: str, perks_identifier: Set[str]) -> Set[Perk]:
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

    def get_perks(self, identifier: str, perks_identifier: Set[str]) -> Set[Perk]:
        classifier = self.get(identifier)

        all_perks = classifier.perks

        perks = set()
        for perk in all_perks:
            if perk.identifier in perks_identifier:
                perks.add(perk)

        return perks


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

    def get_perks(self, identifier: str, perks_identifier: Set[str]) -> Set[Perk]:

        perks = (
            self.session.query(Perk)
            .filter(Perk.classifier_id == CiladaClassifier.id)
            .filter(Perk.identifier.in_(list(perks_identifier)))
            .filter(CiladaClassifier.identifier == identifier)
            .all()
        )

        return perks
