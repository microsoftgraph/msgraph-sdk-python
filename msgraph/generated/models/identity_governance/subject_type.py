from enum import Enum

class SubjectType(str, Enum):
    User = "user",
    UnknownFutureValue = "unknownFutureValue",
    ProvisioningObject = "provisioningObject",

