from enum import Enum

class RecordingStatus(Enum):
    Unknown = "unknown",
    NotRecording = "notRecording",
    Recording = "recording",
    Failed = "failed",
    UnknownFutureValue = "unknownFutureValue",

