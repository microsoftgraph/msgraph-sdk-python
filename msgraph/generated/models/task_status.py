from enum import Enum

class TaskStatus(str, Enum):
    NotStarted = "notStarted",
    InProgress = "inProgress",
    Completed = "completed",
    WaitingOnOthers = "waitingOnOthers",
    Deferred = "deferred",

