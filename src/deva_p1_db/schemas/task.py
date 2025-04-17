
from pydantic import BaseModel
from uuid import UUID


class TaskInput(BaseModel):
    task_id: UUID

class TaskOutput(BaseModel):
    task_id: UUID