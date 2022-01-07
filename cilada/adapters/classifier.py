from typing import List
from pydantic import BaseModel

from cilada import domain
from cilada.adapters import perks as perks_adapter


class BaseClassifier(BaseModel):
    perks: List[perks_adapter.PerkBase]
    cilada_threshold: int

    class Config:
        arbitrary_types_allowed = True


def adapt_perk_base(perks):
    return list(
        map(
            lambda x: perks_adapter.PerkBase(
                description=x.description, cilada_points=x.cilada_points
            ),
            perks,
        )
    )


def to_view(classifier: domain.CiladaClassifier):
    perks = classifier.perks

    perks_adapted = adapt_perk_base(perks)

    return BaseClassifier(
        perks=perks_adapted, cilada_threshold=classifier.cilada_threshold
    )
