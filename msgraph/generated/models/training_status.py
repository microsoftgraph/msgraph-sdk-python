from enum import Enum

class TrainingStatus(Enum):
    Unknown = "unknown",
    Assigned = "assigned",
    InProgress = "inProgress",
    Completed = "completed",
    Overdue = "overdue",
    UnknownFutureValue = "unknownFutureValue",

