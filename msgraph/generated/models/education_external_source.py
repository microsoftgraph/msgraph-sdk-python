from enum import Enum

class EducationExternalSource(str, Enum):
    Sis = "sis",
    Manual = "manual",
    UnknownFutureValue = "unknownFutureValue",

