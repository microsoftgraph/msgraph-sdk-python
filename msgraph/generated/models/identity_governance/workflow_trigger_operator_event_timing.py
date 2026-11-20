from enum import Enum

class WorkflowTriggerOperatorEventTiming(str, Enum):
    Before = "before",
    After = "after",
    On = "on",
    UnknownFutureValue = "unknownFutureValue",

