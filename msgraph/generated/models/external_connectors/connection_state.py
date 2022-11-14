from enum import Enum

class ConnectionState(Enum):
    Draft = "draft",
    Ready = "ready",
    Obsolete = "obsolete",
    LimitExceeded = "limitExceeded",
    UnknownFutureValue = "unknownFutureValue",

