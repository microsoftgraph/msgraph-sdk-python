from enum import Enum

class ProtocolType(str, Enum):
    Tcp = "tcp",
    Udp = "udp",
    UnknownFutureValue = "unknownFutureValue",

