from typing import Annotated
from pydantic import BaseModel, Field


class Todo(BaseModel):
    id: Annotated[str, Field(min_length=36)]
    title: str = Field(max_length=90)
    details: str
    isComplete: bool = False