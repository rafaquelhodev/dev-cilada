from abc import ABC
import abc
from typing import Set

from cilada.domain import CiladaClassifier


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
