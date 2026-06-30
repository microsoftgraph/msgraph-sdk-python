from enum import Enum

class FedRampLevel(str, Enum):
    None_ = "none",
    High = "high",
    LiSaas = "liSaas",
    Low = "low",
    Moderate = "moderate",
    NotSupported = "notSupported",
    UnknownFutureValue = "unknownFutureValue",

