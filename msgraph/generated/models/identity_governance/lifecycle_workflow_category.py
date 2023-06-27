from enum import Enum

class LifecycleWorkflowCategory(str, Enum):
    Joiner = "joiner",
    Leaver = "leaver",
    UnknownFutureValue = "unknownFutureValue",
    Mover = "mover",

