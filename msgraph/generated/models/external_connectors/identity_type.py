from enum import Enum

class IdentityType(Enum):
    User = "user",
    Group = "group",
    ExternalGroup = "externalGroup",
    UnknownFutureValue = "unknownFutureValue",

