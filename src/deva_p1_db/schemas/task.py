
from typing import Optional
from uuid import UUID

from pydantic import BaseModel


class TaskToAi(BaseModel):
    task_id: UUID

class TaskToBack(BaseModel):
    task_id: UUID
    done: bool
    status: Optional[str]