from typing import List, Optional
from pydantic import BaseModel

class Card(BaseModel):
    id: str
    name: str
    manaCost: Optional[str] = None
    cmc: Optional[float] = None
    types: Optional[List[str]] = None
    supertypes: Optional[List[str]] = None
    colors: Optional[List[str]] = None
    colorIdentity: Optional[List[str]] = None
    rarity: Optional[str] = None  