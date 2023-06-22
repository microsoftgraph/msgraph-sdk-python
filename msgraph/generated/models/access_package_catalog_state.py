from enum import Enum

class AccessPackageCatalogState(str, Enum):
    Unpublished = "unpublished",
    Published = "published",
    UnknownFutureValue = "unknownFutureValue",

