from enum import Enum

class TeamsAppResourceSpecificPermissionType(str, Enum):
    Delegated = "delegated",
    Application = "application",
    UnknownFutureValue = "unknownFutureValue",

