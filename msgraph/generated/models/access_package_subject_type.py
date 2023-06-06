from enum import Enum

class AccessPackageSubjectType(str, Enum):
    NotSpecified = "notSpecified",
    User = "user",
    ServicePrincipal = "servicePrincipal",
    UnknownFutureValue = "unknownFutureValue",

