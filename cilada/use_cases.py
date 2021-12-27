from typing import Set

from cilada.domain import CiladaClassifier, JobProposal, Perk
from cilada.exceptions import NotFound
from cilada.repository import ClassifierRepository


class CreateClassifier:
    def __init__(
        self, perks: Set[Perk], cilada_threshold: int, repository: ClassifierRepository
    ) -> None:
        self.perks = perks
        self.cilada_threshold = cilada_threshold
        self.repository = repository

    def execute(self):
        cilada_classifier = CiladaClassifier(perks=self.perks, cilada_threshold=20)
        identifier = self.repository.add(classifier=cilada_classifier)
        return identifier


class FindClassifier:
    def __init__(self, identifier: str, repository: ClassifierRepository) -> None:
        self.identifier = identifier
        self.repository = repository

    def execute(self):
        classifier = self.repository.get(identifier=self.identifier)

        if not classifier:
            raise NotFound("Classifier not found")

        return classifier


class ClassifyJobProposal:
    def __init__(
        self,
        identifier: str,
        repository: ClassifierRepository,
        perks: Set[Perk],
        classifier_finder: FindClassifier,
    ) -> None:
        self.identifier = identifier
        self.repository = repository
        self.perks = perks
        self.classifier_finder = classifier_finder

    def execute(self):
        classifier = self.classifier_finder.execute()

        job_proposal = JobProposal(classifier=classifier, perks=self.perks)

        return job_proposal.is_cilada()
