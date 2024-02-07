from enum import Enum

class EducationModuleStatus(str, Enum):
    Draft = "draft",
    Published = "published",
    UnknownFutureValue = "unknownFutureValue",

