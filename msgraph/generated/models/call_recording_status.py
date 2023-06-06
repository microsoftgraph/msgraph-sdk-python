from enum import Enum

class CallRecordingStatus(str, Enum):
    Success = "success",
    Failure = "failure",
    Initial = "initial",
    ChunkFinished = "chunkFinished",
    UnknownFutureValue = "unknownFutureValue",

