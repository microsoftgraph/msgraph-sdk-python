from enum import Enum

class CallState(Enum):
    Incoming = "incoming",
    Establishing = "establishing",
    Established = "established",
    Hold = "hold",
    Transferring = "transferring",
    TransferAccepted = "transferAccepted",
    Redirecting = "redirecting",
    Terminating = "terminating",
    Terminated = "terminated",
    UnknownFutureValue = "unknownFutureValue",

