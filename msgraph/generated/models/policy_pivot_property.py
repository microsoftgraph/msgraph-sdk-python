from enum import Enum

class PolicyPivotProperty(str, Enum):
    None_ = "none",
    Activity = "activity",
    Location = "location",
    UnknownFutureValue = "unknownFutureValue",

