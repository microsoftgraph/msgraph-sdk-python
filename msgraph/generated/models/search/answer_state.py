from enum import Enum

class AnswerState(str, Enum):
    Published = "published",
    Draft = "draft",
    Excluded = "excluded",
    UnknownFutureValue = "unknownFutureValue",

