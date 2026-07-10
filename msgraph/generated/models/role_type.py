from enum import Enum

class RoleType(str, Enum):
    Active = "active",
    Eligible = "eligible",
    Application = "application",
    Delegated = "delegated",
    UnknownFutureValue = "unknownFutureValue",

