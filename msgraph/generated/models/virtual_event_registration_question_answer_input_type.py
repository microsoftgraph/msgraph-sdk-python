from enum import Enum

class VirtualEventRegistrationQuestionAnswerInputType(str, Enum):
    Text = "text",
    MultilineText = "multilineText",
    SingleChoice = "singleChoice",
    MultiChoice = "multiChoice",
    Boolean = "boolean",
    UnknownFutureValue = "unknownFutureValue",

