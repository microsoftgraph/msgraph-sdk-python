from enum import Enum

class PciVersion(str, Enum):
    None_ = "none",
    V3_2_1 = "v3_2_1",
    V4 = "v4",
    NotSupported = "notSupported",
    UnknownFutureValue = "unknownFutureValue",

