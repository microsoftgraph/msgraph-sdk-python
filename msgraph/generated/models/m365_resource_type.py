from enum import Enum

class M365ResourceType(str, Enum):
    None_ = "none",
    Group = "group",
    User = "user",
    UnknownFutureValue = "unknownFutureValue",

