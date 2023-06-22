from enum import Enum

class ConnectionDirection(str, Enum):
    Unknown = "unknown",
    Inbound = "inbound",
    Outbound = "outbound",
    UnknownFutureValue = "unknownFutureValue",

