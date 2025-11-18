from enum import Enum

class ActivationUserScopeType(str, Enum):
    AllUsers = "allUsers",
    FailedUsers = "failedUsers",
    UnknownFutureValue = "unknownFutureValue",

