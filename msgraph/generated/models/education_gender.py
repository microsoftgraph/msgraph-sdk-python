from enum import Enum

class EducationGender(str, Enum):
    Female = "female",
    Male = "male",
    Other = "other",
    UnknownFutureValue = "unknownFutureValue",

