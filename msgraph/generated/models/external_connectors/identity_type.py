from enum import Enum

class IdentityType(str, Enum):
    User = "user",
    Group = "group",
    ExternalGroup = "externalGroup",
    UnknownFutureValue = "unknownFutureValue",

