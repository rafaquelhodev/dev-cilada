from typing import List
from pydantic import BaseModel
from cilada.domain import Perk


class PerkBase(BaseModel):
    description: str
    cilada_points: int


class PerkView(PerkBase):
    identifier: str


def adapt_base_to_domain(perks: List[PerkBase]):
    return set(map(lambda x: Perk(x.description, x.cilada_points), perks))
