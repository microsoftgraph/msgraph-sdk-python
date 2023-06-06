from enum import Enum

class EventPropagationStatus(str, Enum):
    None_ = "none",
    InProcessing = "inProcessing",
    Failed = "failed",
    Success = "success",
    UnknownFutureValue = "unknownFutureValue",

