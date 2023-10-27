from enum import Enum

class HostPortProtocol(str, Enum):
    Tcp = "tcp",
    Udp = "udp",
    UnknownFutureValue = "unknownFutureValue",

