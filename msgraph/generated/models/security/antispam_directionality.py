from enum import Enum

class AntispamDirectionality(str, Enum):
    Unknown = "unknown",
    Inbound = "inbound",
    Outbound = "outbound",
    IntraOrg = "intraOrg",
    UnknownFutureValue = "unknownFutureValue",

