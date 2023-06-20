from enum import Enum

class PrintTaskProcessingState(str, Enum):
    Pending = "pending",
    Processing = "processing",
    Completed = "completed",
    Aborted = "aborted",
    UnknownFutureValue = "unknownFutureValue",

