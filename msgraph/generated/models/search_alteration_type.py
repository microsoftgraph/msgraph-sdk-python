from enum import Enum

class SearchAlterationType(str, Enum):
    Suggestion = "suggestion",
    Modification = "modification",
    UnknownFutureValue = "unknownFutureValue",

