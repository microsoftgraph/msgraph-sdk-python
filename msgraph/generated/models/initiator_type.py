from enum import Enum

class InitiatorType(Enum):
    User = "user",
    Application = "application",
    System = "system",
    UnknownFutureValue = "unknownFutureValue",

