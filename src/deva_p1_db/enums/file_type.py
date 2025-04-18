

from enum import Enum


class FileType(str, Enum):
    image_png = "image_png"
    image_jpg = "image_jpg"
    image_webp = "image_webp"

    audio_mp3 = "mp3"
    audio_wav = "wav"
    audio_ogg = "audio_ogg"
    audio_flac = "audio_flac"
    audio_aac = "audio_aac"
    audio_m4a = "audio_m4a"
    audio_opus = "audio_opus"
    audio_audio_webm = "audio_audio_webm"

    video_mp4 = "video_mp4"
    video_mkv = "video_mkv"
    video_avi = "video_avi"
    video_mov = "video_mov"
    video_webm = "video_webm"

    undefined = "undefined"


