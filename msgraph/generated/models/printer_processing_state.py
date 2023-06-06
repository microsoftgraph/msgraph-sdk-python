from enum import Enum

class PrinterProcessingState(str, Enum):
    Unknown = "unknown",
    Idle = "idle",
    Processing = "processing",
    Stopped = "stopped",
    UnknownFutureValue = "unknownFutureValue",

