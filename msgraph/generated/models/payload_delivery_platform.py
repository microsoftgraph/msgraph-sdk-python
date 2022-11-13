from enum import Enum

class PayloadDeliveryPlatform(Enum):
    Unknown = "unknown",
    Sms = "sms",
    Email = "email",
    Teams = "teams",
    UnknownFutureValue = "unknownFutureValue",

