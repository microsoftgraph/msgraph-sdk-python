from enum import Enum

class ContactRelationship(str, Enum):
    Parent = "parent",
    Relative = "relative",
    Aide = "aide",
    Doctor = "doctor",
    Guardian = "guardian",
    Child = "child",
    Other = "other",
    UnknownFutureValue = "unknownFutureValue",

