from enum import Enum

class DeliveryAction(str, Enum):
    Unknown = "unknown",
    DeliveredToJunk = "deliveredToJunk",
    Delivered = "delivered",
    Blocked = "blocked",
    Replaced = "replaced",
    UnknownFutureValue = "unknownFutureValue",

