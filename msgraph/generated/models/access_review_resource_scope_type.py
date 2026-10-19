from enum import Enum

class AccessReviewResourceScopeType(str, Enum):
    Group = "group",
    Catalog = "catalog",
    ServicePrincipal = "servicePrincipal",
    DirectoryRole = "directoryRole",
    AccessPackageAssignmentPolicy = "accessPackageAssignmentPolicy",
    UnknownFutureValue = "unknownFutureValue",

