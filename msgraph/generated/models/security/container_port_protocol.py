from enum import Enum

class ContainerPortProtocol(str, Enum):
    Udp = "udp",
    Tcp = "tcp",
    Sctp = "sctp",
    UnknownFutureValue = "unknownFutureValue",

