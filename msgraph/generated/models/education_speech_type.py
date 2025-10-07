from enum import Enum

class EducationSpeechType(str, Enum):
    Informative = "informative",
    Personal = "personal",
    Persuasive = "persuasive",
    UnknownFutureValue = "unknownFutureValue",

