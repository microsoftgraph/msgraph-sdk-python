from enum import Enum

class AnswerInputType(str, Enum):
    Text = "text",
    RadioButton = "radioButton",
    UnknownFutureValue = "unknownFutureValue",

