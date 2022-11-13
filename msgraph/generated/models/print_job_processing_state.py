from enum import Enum

class PrintJobProcessingState(Enum):
    Unknown = "unknown",
    Pending = "pending",
    Processing = "processing",
    Paused = "paused",
    Stopped = "stopped",
    Completed = "completed",
    Canceled = "canceled",
    Aborted = "aborted",
    UnknownFutureValue = "unknownFutureValue",

