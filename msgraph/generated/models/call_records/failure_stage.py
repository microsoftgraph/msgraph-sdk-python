from enum import Enum

class FailureStage(Enum):
    Unknown = "unknown",
    CallSetup = "callSetup",
    Midcall = "midcall",
    UnknownFutureValue = "unknownFutureValue",

