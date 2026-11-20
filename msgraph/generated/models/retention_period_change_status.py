from enum import Enum

class RetentionPeriodChangeStatus(str, Enum):
    None_ = "none",
    InProgress = "inProgress",
    Failed = "failed",
    Completed = "completed",
    UnknownFutureValue = "unknownFutureValue",

