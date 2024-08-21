from enum import Enum

class BackupServiceConsumer(str, Enum):
    Unknown = "unknown",
    Firstparty = "firstparty",
    Thirdparty = "thirdparty",
    UnknownFutureValue = "unknownFutureValue",

