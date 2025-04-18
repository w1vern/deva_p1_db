
from typing import Optional
from pydantic import BaseModel
from uuid import UUID


class TaskToAi(BaseModel):
    task_id: UUID

class TaskToBack(BaseModel):
    task_id: UUID
    done: bool
    status: Optional[str]