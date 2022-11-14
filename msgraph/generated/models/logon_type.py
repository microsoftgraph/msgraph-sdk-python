from enum import Enum

class LogonType(Enum):
    Unknown = "unknown",
    Interactive = "interactive",
    RemoteInteractive = "remoteInteractive",
    Network = "network",
    Batch = "batch",
    Service = "service",
    UnknownFutureValue = "unknownFutureValue",

