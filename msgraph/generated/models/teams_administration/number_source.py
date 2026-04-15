from enum import Enum

class NumberSource(str, Enum):
    Online = "online",
    OnPremises = "onPremises",
    UnknownFutureValue = "unknownFutureValue",

