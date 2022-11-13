from enum import Enum

class AccessType(Enum):
    Grant = "grant",
    Deny = "deny",
    UnknownFutureValue = "unknownFutureValue",

