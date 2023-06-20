from enum import Enum

class RejectReason(str, Enum):
    None_ = "none",
    Busy = "busy",
    Forbidden = "forbidden",
    UnknownFutureValue = "unknownFutureValue",

