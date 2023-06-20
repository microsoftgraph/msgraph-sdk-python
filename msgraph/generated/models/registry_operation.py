from enum import Enum

class RegistryOperation(str, Enum):
    Unknown = "unknown",
    Create = "create",
    Modify = "modify",
    Delete = "delete",
    UnknownFutureValue = "unknownFutureValue",

