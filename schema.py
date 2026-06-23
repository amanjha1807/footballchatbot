from typing import List, Optional, Literal
from pydantic import BaseModel, Field

class FootballResponse(BaseModel):
    response_type: Literal["chat", "player"]

    answer: str

    player_name: Optional[str] = None
    club: Optional[str] = None
    position: Optional[str] = None
    achievements: Optional[List[str]] = None