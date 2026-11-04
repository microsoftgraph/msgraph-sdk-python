from enum import Enum

class ApplicationMode(str, Enum):
    Manual = "manual",
    Automatic = "automatic",
    Recommended = "recommended",
    UnknownFutureValue = "unknownFutureValue",

