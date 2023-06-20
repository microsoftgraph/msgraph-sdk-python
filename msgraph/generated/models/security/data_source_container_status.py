from enum import Enum

class DataSourceContainerStatus(str, Enum):
    Active = "active",
    Released = "released",
    UnknownFutureValue = "unknownFutureValue",

