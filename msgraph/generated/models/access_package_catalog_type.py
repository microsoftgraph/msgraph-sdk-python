from enum import Enum

class AccessPackageCatalogType(Enum):
    UserManaged = "userManaged",
    ServiceDefault = "serviceDefault",
    ServiceManaged = "serviceManaged",
    UnknownFutureValue = "unknownFutureValue",

