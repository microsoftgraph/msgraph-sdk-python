from enum import Enum

class PortInStatus(str, Enum):
    Completed = "completed",
    FirmOrderCommitmentAccepted = "firmOrderCommitmentAccepted",
    UnknownFutureValue = "unknownFutureValue",

