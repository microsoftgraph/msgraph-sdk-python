from enum import Enum

class SharePointMigrationJobErrorLevel(str, Enum):
    Important = "important",
    Warning = "warning",
    Error = "error",
    FatalError = "fatalError",
    UnknownFutureValue = "unknownFutureValue",

