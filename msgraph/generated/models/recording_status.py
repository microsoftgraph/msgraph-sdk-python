from enum import Enum

class RecordingStatus(str, Enum):
    Unknown = "unknown",
    NotRecording = "notRecording",
    Recording = "recording",
    Failed = "failed",
    UnknownFutureValue = "unknownFutureValue",

