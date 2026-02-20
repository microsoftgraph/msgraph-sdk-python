from enum import Enum

class ResourceAccessType(str, Enum):
    None_ = "none",
    Read = "read",
    Write = "write",
    Create = "create",
    UnknownFutureValue = "unknownFutureValue",

