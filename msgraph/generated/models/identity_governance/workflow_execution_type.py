from enum import Enum

class WorkflowExecutionType(str, Enum):
    Scheduled = "scheduled",
    OnDemand = "onDemand",
    UnknownFutureValue = "unknownFutureValue",

