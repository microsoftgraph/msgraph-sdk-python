from enum import Enum

class EventStatusType(str, Enum):
    Pending = "pending",
    Error = "error",
    Success = "success",
    NotAvaliable = "notAvaliable",
    UnknownFutureValue = "unknownFutureValue",

