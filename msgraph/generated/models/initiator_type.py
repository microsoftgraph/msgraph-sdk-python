from enum import Enum

class InitiatorType(str, Enum):
    User = "user",
    Application = "application",
    System = "system",
    UnknownFutureValue = "unknownFutureValue",

