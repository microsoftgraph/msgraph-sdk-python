from enum import Enum

class ExecutionMode(str, Enum):
    EvaluateInline = "evaluateInline",
    EvaluateOffline = "evaluateOffline",
    UnknownFutureValue = "unknownFutureValue",

