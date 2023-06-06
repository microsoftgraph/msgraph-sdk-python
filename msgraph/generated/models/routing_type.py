from enum import Enum

class RoutingType(str, Enum):
    Forwarded = "forwarded",
    Lookup = "lookup",
    SelfFork = "selfFork",
    UnknownFutureValue = "unknownFutureValue",

