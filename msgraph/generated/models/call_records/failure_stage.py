from enum import Enum

class FailureStage(str, Enum):
    Unknown = "unknown",
    CallSetup = "callSetup",
    Midcall = "midcall",
    UnknownFutureValue = "unknownFutureValue",

