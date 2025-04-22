
from enum import Enum


class TaskType(str, Enum):
    transcribe = 'transcribe'
    summary = 'summary'
    frames_extract = 'frames_extract'

    

