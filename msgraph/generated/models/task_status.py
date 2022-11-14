from enum import Enum

class TaskStatus(Enum):
    NotStarted = "notStarted",
    InProgress = "inProgress",
    Completed = "completed",
    WaitingOnOthers = "waitingOnOthers",
    Deferred = "deferred",

