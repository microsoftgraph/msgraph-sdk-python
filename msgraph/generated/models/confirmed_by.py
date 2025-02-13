from enum import Enum

class ConfirmedBy(str, Enum):
    None_ = "none",
    User = "user",
    Manager = "manager",
    UnknownFutureValue = "unknownFutureValue",

