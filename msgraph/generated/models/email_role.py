from enum import Enum

class EmailRole(str, Enum):
    Unknown = "unknown",
    Sender = "sender",
    Recipient = "recipient",
    UnknownFutureValue = "unknownFutureValue",

