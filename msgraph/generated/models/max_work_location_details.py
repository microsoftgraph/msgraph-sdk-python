from enum import Enum

class MaxWorkLocationDetails(str, Enum):
    Unknown = "unknown",
    None_ = "none",
    Approximate = "approximate",
    Specific = "specific",
    UnknownFutureValue = "unknownFutureValue",

