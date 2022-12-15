from enum import Enum

class ActivityType(Enum):
    Signin = "signin",
    User = "user",
    UnknownFutureValue = "unknownFutureValue",
    ServicePrincipal = "servicePrincipal",

