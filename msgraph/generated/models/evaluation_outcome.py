from enum import Enum

class EvaluationOutcome(str, Enum):
    Approved = "approved",
    Denied = "denied",
    UnknownFutureValue = "unknownFutureValue",

