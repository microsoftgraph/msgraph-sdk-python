from enum import Enum

class ContentProcessingErrorType(str, Enum):
    Transient = "transient",
    Permanent = "permanent",
    UnknownFutureValue = "unknownFutureValue",

