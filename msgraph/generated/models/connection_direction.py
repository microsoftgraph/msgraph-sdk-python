from enum import Enum

class ConnectionDirection(Enum):
    Unknown = "unknown",
    Inbound = "inbound",
    Outbound = "outbound",
    UnknownFutureValue = "unknownFutureValue",

