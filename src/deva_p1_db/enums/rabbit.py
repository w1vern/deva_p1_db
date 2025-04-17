

from .task_type import TaskType
from faststream.rabbit import RabbitQueue


class RabbitQueuesToAi:
    transcribe_task = RabbitQueue(
        name=f"{TaskType.transcribe.value}_task"
    )
    summary_task = RabbitQueue(
        name=f"{TaskType.summary.value}_task"
    )
    frames_extract_task = RabbitQueue(
        name=f"{TaskType.frames_extract.value}_task"
    )

class RabbitQueuesToBack:
    done_task = RabbitQueue(
        name="done_task"
    )
    error_task = RabbitQueue(
        name="error_task"
    )
    progress_task = RabbitQueue(
        name="progress_task"
    )
