from enum import Enum

class NetworkConnectionType(str, Enum):
    Unknown = "unknown",
    Wired = "wired",
    Wifi = "wifi",
    Mobile = "mobile",
    Tunnel = "tunnel",
    UnknownFutureValue = "unknownFutureValue",

