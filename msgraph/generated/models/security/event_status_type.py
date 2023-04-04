from enum import Enum

class EventStatusType(Enum):
    Pending = "pending",
    Error = "error",
    Success = "success",
    NotAvaliable = "notAvaliable",
    UnknownFutureValue = "unknownFutureValue",

