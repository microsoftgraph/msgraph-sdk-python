from enum import Enum

class LifecycleTaskCategory(str, Enum):
    Joiner = "joiner",
    Leaver = "leaver",
    UnknownFutureValue = "unknownFutureValue",
    Mover = "mover",

