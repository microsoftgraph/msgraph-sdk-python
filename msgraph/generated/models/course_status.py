from enum import Enum

class CourseStatus(str, Enum):
    NotStarted = "notStarted",
    InProgress = "inProgress",
    Completed = "completed",
    UnknownFutureValue = "unknownFutureValue",

