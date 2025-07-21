from enum import Enum

class AccessPackageCatalogType(str, Enum):
    UserManaged = "userManaged",
    ServiceDefault = "serviceDefault",
    ServiceManaged = "serviceManaged",
    UnknownFutureValue = "unknownFutureValue",

