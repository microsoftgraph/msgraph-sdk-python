from enum import Enum

class WorkLocationSource(str, Enum):
    None_ = "none",
    Manual = "manual",
    Scheduled = "scheduled",
    Automatic = "automatic",
    UnknownFutureValue = "unknownFutureValue",

