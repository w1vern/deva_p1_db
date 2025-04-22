
from enum import Enum


class TaskType(str, Enum):
    transcribe = 'transcribe'
    frames_extract = 'frames_extract'
    summary = 'summary'
    summary_edit = 'summary_edit'

    

