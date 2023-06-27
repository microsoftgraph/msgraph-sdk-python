from enum import Enum

class SensitivityLabelAssignmentMethod(str, Enum):
    Standard = "standard",
    Privileged = "privileged",
    Auto = "auto",
    UnknownFutureValue = "unknownFutureValue",

