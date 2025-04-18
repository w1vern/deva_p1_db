

from enum import Enum


class FileType(str, Enum):
    png = "png"
    jpg = "jpg"
    webp = "webp"

    mp3 = "mp3"
    wav = "wav"
    ogg = "ogg"
    flac = "flac"
    aac = "aac"
    m4a = "m4a"
    opus = "opus"
    audio_webm = "audio_webm"

    mp4 = "mp4"
    mkv = "mkv"
    avi = "avi"
    mov = "mov"
    video_webm = "video_webm"


