

from enum import Enum
from dataclasses import dataclass
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

FILE_TYPES = [
    FileType('image_png',     'image/png',               '.png',     "image"),
    FileType('image_jpg',     'image/jpeg',              '.jpg',     "image"),
    FileType('image_webp',    'image/webp',              '.webp',    "image"),

    FileType('audio_mp3',     'audio/mpeg',              '.mp3',     "audio"),
    FileType('audio_wav',     'audio/wav',               '.wav',     "audio"),
    FileType('audio_ogg',     'audio/ogg',               '.ogg',     "audio"),
    FileType('audio_flac',    'audio/flac',              '.flac',    "audio"),
    FileType('audio_aac',     'audio/aac',               '.aac',     "audio"),
    FileType('audio_m4a',     'audio/mp4',               '.m4a',     "audio"),
    FileType('audio_opus',    'audio/opus',              '.opus',    "audio"),
    FileType('audio_webm',    'audio/webm',              '.webm',    "audio"),

    FileType('video_mp4',     'video/mp4',               '.mp4',     "video"),
    FileType('video_mkv',     'video/x-matroska',        '.mkv',     "video"),
    FileType('video_avi',     'video/x-msvideo',         '.avi',     "video"),
    FileType('video_mov',     'video/quicktime',         '.mov',     "video"),
    FileType('video_webm',    'video/webm',              '.webm',    "video"),

    FileType('text_plain',    'text/plain',              '.txt',     "summary"),
    FileType('text_json',     'application/json',        '.json',    "transcribe"),
    FileType('text_md',       'text/markdown',           '.md',      "summary"),

    FileType('undefined',     'application/octet-stream','.bin',     "undefined")
]

LOOKUP_INDEXES = {
    'internal': {ft.internal: ft for ft in FILE_TYPES},
    'mime':     {ft.mime:     ft for ft in FILE_TYPES},
    'extension':      {ft.extension:      ft for ft in FILE_TYPES},
}

def resolve_file_type(value: str, type_hint: Optional[str] = None) -> Optional[FileType]:
    if type_hint:
        return LOOKUP_INDEXES.get(type_hint, {}).get(value)
    for index in LOOKUP_INDEXES.values():
        if value in index:
            return index[value]
    return None

print(resolve_file_type('image/png'), "\n")
print(resolve_file_type(".flac"),"\n")
print(resolve_file_type(".jpg"),"\n")
print(resolve_file_type("text/markdown"),"\n")
print(resolve_file_type("text_plain"),"\n")
print(resolve_file_type(".webm"),"\n")


