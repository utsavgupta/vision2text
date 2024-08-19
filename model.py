from langchain_core.pydantic_v1 import BaseModel, Field
from typing import List

class ExtractedText(BaseModel):
    goals: List[str] = Field(description="Goals of the team.")
    achievements: List[str] = Field(description="Achievements of the team.")
    feedback: List[str] = Field(description="Feedback received by the team.")
