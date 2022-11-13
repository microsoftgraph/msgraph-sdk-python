from enum import Enum

class RegistryOperation(Enum):
    Unknown = "unknown",
    Create = "create",
    Modify = "modify",
    Delete = "delete",
    UnknownFutureValue = "unknownFutureValue",

