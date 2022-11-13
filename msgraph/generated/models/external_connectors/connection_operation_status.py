from enum import Enum

class ConnectionOperationStatus(Enum):
    Unspecified = "unspecified",
    Inprogress = "inprogress",
    Completed = "completed",
    Failed = "failed",
    UnknownFutureValue = "unknownFutureValue",

