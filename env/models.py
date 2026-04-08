from pydantic import BaseModel
from typing import List, Dict


class Assignment(BaseModel):
    name: str
    deadline: int
    difficulty: int


class Observation(BaseModel):
    assignments: List[Assignment]
    time_available: int
    team_status: Dict[str, str]


class Action(BaseModel):
    prioritize: str
    allocate_time: int
    assign_to: str


class Reward(BaseModel):
    score: float
    feedback: str