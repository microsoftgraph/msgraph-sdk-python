from enum import Enum

class LabelActionSource(str, Enum):
    Manual = "manual",
    Automatic = "automatic",
    Recommended = "recommended",
    None_ = "none",
    UnknownFutureValue = "unknownFutureValue",

