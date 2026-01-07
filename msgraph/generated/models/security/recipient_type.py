from enum import Enum

class RecipientType(str, Enum):
    User = "user",
    RoleGroup = "roleGroup",
    UnknownFutureValue = "unknownFutureValue",

