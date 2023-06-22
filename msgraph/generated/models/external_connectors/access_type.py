from enum import Enum

class AccessType(str, Enum):
    Grant = "grant",
    Deny = "deny",
    UnknownFutureValue = "unknownFutureValue",

