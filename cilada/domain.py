from typing import Set
from uuid import uuid4


class Perk:
    def __init__(
        self, description: str, cilada_points: int, identifier: str = None
    ) -> None:
        self.description = description
        self.cilada_points = cilada_points
        self.identifier = identifier if identifier else str(uuid4())


class CiladaClassifier:
    def __init__(
        self,
        perks: Set[Perk],
        cilada_threshold: int,
        identifier: str = None,
    ) -> None:
        self.perks = perks
        self.cilada_threshold = cilada_threshold
        self.identifier = identifier if identifier else str(uuid4())


class JobProposal:
    def __init__(self, classifier: CiladaClassifier, perks: Set[Perk]) -> None:
        self.classifier = classifier
        self.perks = perks

    def is_cilada(self):
        cilada_points = 0

        for perk in self.perks:
            cilada_points += perk.cilada_points

        if cilada_points > self.classifier.cilada_threshold:
            return True

        return False
