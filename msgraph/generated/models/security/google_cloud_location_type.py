from enum import Enum

class GoogleCloudLocationType(str, Enum):
    Unknown = "unknown",
    Regional = "regional",
    Zonal = "zonal",
    Global_ = "global",
    UnknownFutureValue = "unknownFutureValue",

