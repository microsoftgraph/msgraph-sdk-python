from enum import Enum

class Modality(str, Enum):
    Audio = "audio",
    Video = "video",
    VideoBasedScreenSharing = "videoBasedScreenSharing",
    Data = "data",
    UnknownFutureValue = "unknownFutureValue",

