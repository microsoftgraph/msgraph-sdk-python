from enum import Enum

class HostPortStatus(str, Enum):
    Open = "open",
    Filtered = "filtered",
    Closed = "closed",
    UnknownFutureValue = "unknownFutureValue",

