from typing import List
from pydantic import BaseModel


class BaseJobProposal(BaseModel):
    perks: List[str]
    classifier: str
