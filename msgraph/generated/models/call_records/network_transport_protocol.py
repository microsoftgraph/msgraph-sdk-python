from enum import Enum

class NetworkTransportProtocol(str, Enum):
    Unknown = "unknown",
    Udp = "udp",
    Tcp = "tcp",
    UnknownFutureValue = "unknownFutureValue",

