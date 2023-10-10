from enum import Enum

class TrainingAvailabilityStatus(str, Enum):
    Unknown = "unknown",
    NotAvailable = "notAvailable",
    Available = "available",
    Archive = "archive",
    Delete = "delete",
    UnknownFutureValue = "unknownFutureValue",

