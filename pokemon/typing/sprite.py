from typing import List
from pydantic import BaseModel
from typing import List
from pydantic import BaseModel, Field

class GenderRatio(BaseModel):
    M: float
    F: float

class BaseStats(BaseModel):
    hp: int
    atk: int
    def_: int = Field(..., alias="def")
    spa: int
    spd: int
    spe: int

class Abilities(BaseModel):
    ability_0: str = Field(None, alias="0")
    ability_H: str = Field(..., alias="H")

class Sprite(BaseModel):
    num: int
    name: str
    types: List[str]
    genderRatio: GenderRatio
    baseStats: BaseStats
    abilities: Abilities
    heightm: float
    weightkg: float
    color: str
    evos: List[str]
    eggGroups: List[str]
    tier: str
    isNonstandard: str
