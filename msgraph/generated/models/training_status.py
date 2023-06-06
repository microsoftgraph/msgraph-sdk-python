from enum import Enum

class TrainingStatus(str, Enum):
    Unknown = "unknown",
    Assigned = "assigned",
    InProgress = "inProgress",
    Completed = "completed",
    Overdue = "overdue",
    UnknownFutureValue = "unknownFutureValue",

