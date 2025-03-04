from enum import Enum

class TeamsMessageDeliveryAction(str, Enum):
    Unknown = "unknown",
    DeliveredAsSpam = "deliveredAsSpam",
    Delivered = "delivered",
    Blocked = "blocked",
    Replaced = "replaced",
    UnknownFutureValue = "unknownFutureValue",

