from enum import Enum

class ScheduleChangeState(Enum):
    Pending = "pending",
    Approved = "approved",
    Declined = "declined",
    UnknownFutureValue = "unknownFutureValue",

