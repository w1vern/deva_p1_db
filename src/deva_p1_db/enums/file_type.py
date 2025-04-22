from dataclasses import dataclass
from enum import Enum
from typing import Optional


class FileCategory(str, Enum):
    audio = "audio"
    video = "video"
    image = "image"
    transcribe = "transcribe"
    summary = "summary"
    undefined = "undefined"


@dataclass(frozen=True)
class FileType:
    internal: str
    mime: str
    extension: str
    category: str


class FileTypes():
    image_png = FileType('image_png', 'image/png', '.png', "image")
    image_jpg = FileType('image_jpg', 'image/jpeg', '.jpg', "image")
    image_webp = FileType('image_webp', 'image/webp', '.webp', "image")

    audio_mp3 = FileType('audio_mp3', 'audio/mpeg', '.mp3', "audio")
    audio_wav = FileType('audio_wav', 'audio/wav', '.wav', "audio")
    audio_ogg = FileType('audio_ogg', 'audio/ogg', '.ogg', "audio")
    audio_flac = FileType('audio_flac', 'audio/flac', '.flac', "audio")
    audio_aac = FileType('audio_aac', 'audio/aac', '.aac', "audio")
    audio_m4a = FileType('audio_m4a', 'audio/mp4', '.m4a', "audio")
    audio_opus = FileType('audio_opus', 'audio/opus', '.opus', "audio")
    audio_webm = FileType('audio_webm', 'audio/webm', '.webm', "audio")

    video_mp4 = FileType('video_mp4', 'video/mp4', '.mp4', "video")
    video_mkv = FileType('video_mkv', 'video/x-matroska', '.mkv', "video")
    video_avi = FileType('video_avi', 'video/x-msvideo', '.avi', "video")
    video_mov = FileType('video_mov', 'video/quicktime', '.mov', "video")
    video_webm = FileType('video_webm', 'video/webm', '.webm', "video")

    text_plain = FileType('text_plain', 'text/plain', '.txt', "summary")
    text_json = FileType('text_json', 'application/json',
                         '.json', "transcribe")
    text_md = FileType('text_md', 'text/markdown', '.md', "summary")

    undefined = FileType(
        'undefined', 'application/octet-stream', '.bin', "undefined")


FILE_TYPES: list[FileType] = [
    member for member in FileTypes.__dict__.values() if isinstance(member, FileType)]

LOOKUP_INDEXES = {
    'internal': {ft.internal: ft for ft in FILE_TYPES},
    'mime': {ft.mime: ft for ft in FILE_TYPES},
    'extension': {ft.extension: ft for ft in FILE_TYPES},
}


def resolve_file_type(value: str, type_hint: Optional[str] = None) -> Optional[FileType]:
    if type_hint:
        return LOOKUP_INDEXES.get(type_hint, {}).get(value)
    for index in LOOKUP_INDEXES.values():
        if value in index:
            return index[value]
    return None
