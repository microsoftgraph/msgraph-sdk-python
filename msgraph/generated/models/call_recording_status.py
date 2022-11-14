from enum import Enum

class CallRecordingStatus(Enum):
    Success = "success",
    Failure = "failure",
    Initial = "initial",
    ChunkFinished = "chunkFinished",
    UnknownFutureValue = "unknownFutureValue",

