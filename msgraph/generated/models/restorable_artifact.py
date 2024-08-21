from enum import Enum

class RestorableArtifact(str, Enum):
    Message = "message",
    UnknownFutureValue = "unknownFutureValue",

