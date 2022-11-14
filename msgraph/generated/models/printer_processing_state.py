from enum import Enum

class PrinterProcessingState(Enum):
    Unknown = "unknown",
    Idle = "idle",
    Processing = "processing",
    Stopped = "stopped",
    UnknownFutureValue = "unknownFutureValue",

