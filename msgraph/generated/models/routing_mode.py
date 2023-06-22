from enum import Enum

class RoutingMode(str, Enum):
    OneToOne = "oneToOne",
    Multicast = "multicast",
    UnknownFutureValue = "unknownFutureValue",

