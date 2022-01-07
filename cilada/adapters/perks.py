from pydantic import BaseModel
from cilada.domain import Perk


class PerkBase(BaseModel):
    description: str
    cilada_points: int


def adapt_to_domain(perks):
    return set(map(lambda x: Perk(x.description, x.cilada_points), perks))
