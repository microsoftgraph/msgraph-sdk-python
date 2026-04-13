from enum import Enum

class MigrationMode(str, Enum):
    InProgress = "inProgress",
    Completed = "completed",
    UnknownFutureValue = "unknownFutureValue",

