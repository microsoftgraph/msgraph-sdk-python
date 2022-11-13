from enum import Enum

class RoutingType(Enum):
    Forwarded = "forwarded",
    Lookup = "lookup",
    SelfFork = "selfFork",
    UnknownFutureValue = "unknownFutureValue",

