from enum import Enum

class NetworkTransportProtocol(Enum):
    Unknown = "unknown",
    Udp = "udp",
    Tcp = "tcp",
    UnknownFutureValue = "unknownFutureValue",

