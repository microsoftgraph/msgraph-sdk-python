from enum import Enum

class AntispamTeamsDirection(str, Enum):
    Unknown = "unknown",
    Inbound = "inbound",
    Outbound = "outbound",
    Intraorg = "intraorg",
    UnknownFutureValue = "unknownFutureValue",

