from enum import Enum

class ScheduleChangeState(str, Enum):
    Pending = "pending",
    Approved = "approved",
    Declined = "declined",
    UnknownFutureValue = "unknownFutureValue",

