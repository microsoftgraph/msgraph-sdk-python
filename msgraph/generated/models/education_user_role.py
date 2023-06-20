from enum import Enum

class EducationUserRole(str, Enum):
    Student = "student",
    Teacher = "teacher",
    None_ = "none",
    UnknownFutureValue = "unknownFutureValue",

