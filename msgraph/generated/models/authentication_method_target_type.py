from enum import Enum

class AuthenticationMethodTargetType(str, Enum):
    User = "user",
    Group = "group",
    UnknownFutureValue = "unknownFutureValue",

