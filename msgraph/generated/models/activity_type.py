from enum import Enum

class ActivityType(str, Enum):
    Signin = "signin",
    User = "user",
    UnknownFutureValue = "unknownFutureValue",
    ServicePrincipal = "servicePrincipal",

