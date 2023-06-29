from enum import Enum

class IntelligenceProfileKind(str, Enum):
    Actor = "actor",
    Tool = "tool",
    UnknownFutureValue = "unknownFutureValue",

