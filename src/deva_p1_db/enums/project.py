

from enum import Enum


class ProjectType(str, Enum):
    from_audio = "from_audio"
    from_video = "from_video"
    from_transcribe = "from_transcribe"
    undefined = "undefined"