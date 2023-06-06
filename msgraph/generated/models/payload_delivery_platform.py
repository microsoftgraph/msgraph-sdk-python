from enum import Enum

class PayloadDeliveryPlatform(str, Enum):
    Unknown = "unknown",
    Sms = "sms",
    Email = "email",
    Teams = "teams",
    UnknownFutureValue = "unknownFutureValue",

