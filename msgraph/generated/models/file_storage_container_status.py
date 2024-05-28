from enum import Enum

class FileStorageContainerStatus(str, Enum):
    Inactive = "inactive",
    Active = "active",
    UnknownFutureValue = "unknownFutureValue",

