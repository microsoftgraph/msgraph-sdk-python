from enum import Enum

class EmailRole(Enum):
    Unknown = "unknown",
    Sender = "sender",
    Recipient = "recipient",
    UnknownFutureValue = "unknownFutureValue",

