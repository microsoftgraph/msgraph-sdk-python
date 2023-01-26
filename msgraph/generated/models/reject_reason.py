from enum import Enum

class RejectReason(Enum):
    None_ = "none",
    Busy = "busy",
    Forbidden = "forbidden",
    UnknownFutureValue = "unknownFutureValue",

