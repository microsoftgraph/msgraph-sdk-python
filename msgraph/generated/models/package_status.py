from enum import Enum

class PackageStatus(str, Enum):
    None_ = "none",
    Some = "some",
    All = "all",
    UnknownFutureValue = "unknownFutureValue",

