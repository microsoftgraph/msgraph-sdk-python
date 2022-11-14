from enum import Enum

class CallTranscriptionState(Enum):
    NotStarted = "notStarted",
    Active = "active",
    Inactive = "inactive",
    UnknownFutureValue = "unknownFutureValue",

