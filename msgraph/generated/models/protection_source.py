from enum import Enum

class ProtectionSource(str, Enum):
    None_ = "none",
    Manual = "manual",
    DynamicRule = "dynamicRule",
    UnknownFutureValue = "unknownFutureValue",

