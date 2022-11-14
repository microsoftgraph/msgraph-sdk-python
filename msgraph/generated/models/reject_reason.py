from enum import Enum

class RejectReason(Enum):
    None_escaped = "none",
    Busy = "busy",
    Forbidden = "forbidden",
    UnknownFutureValue = "unknownFutureValue",

