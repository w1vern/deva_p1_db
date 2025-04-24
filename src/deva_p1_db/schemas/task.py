
from typing import Optional
from uuid import UUID

from pydantic import BaseModel


class TaskToAi(BaseModel):
    task_id: UUID

class TaskReadyToBack(BaseModel):
    task_id: UUID

class TaskStatusToBack(BaseModel):
    task_id: UUID
    progress: float

class TaskErrorToBack(BaseModel):
    task_id: UUID
    error: str