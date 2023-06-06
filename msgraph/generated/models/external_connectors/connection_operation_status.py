from enum import Enum

class ConnectionOperationStatus(str, Enum):
    Unspecified = "unspecified",
    Inprogress = "inprogress",
    Completed = "completed",
    Failed = "failed",
    UnknownFutureValue = "unknownFutureValue",

