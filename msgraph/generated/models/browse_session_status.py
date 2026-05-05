from enum import Enum

class BrowseSessionStatus(str, Enum):
    Creating = "creating",
    Created = "created",
    Failed = "failed",
    UnknownFutureValue = "unknownFutureValue",

