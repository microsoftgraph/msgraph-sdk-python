from enum import Enum

class CallTranscriptionState(str, Enum):
    NotStarted = "notStarted",
    Active = "active",
    Inactive = "inactive",
    UnknownFutureValue = "unknownFutureValue",

