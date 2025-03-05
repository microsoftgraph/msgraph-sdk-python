from enum import Enum

class TeamsDeliveryLocation(str, Enum):
    Unknown = "unknown",
    Teams = "teams",
    Quarantine = "quarantine",
    Failed = "failed",
    UnknownFutureValue = "unknownFutureValue",

