from enum import Enum

class CustomTaskExtensionOperationStatus(str, Enum):
    Completed = "completed",
    Failed = "failed",
    UnknownFutureValue = "unknownFutureValue",

