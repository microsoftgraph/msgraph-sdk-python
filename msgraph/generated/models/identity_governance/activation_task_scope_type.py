from enum import Enum

class ActivationTaskScopeType(str, Enum):
    AllTasks = "allTasks",
    FailedTasks = "failedTasks",
    UnknownFutureValue = "unknownFutureValue",

