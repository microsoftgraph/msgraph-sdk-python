from enum import Enum

class AccessPackageSubjectLifecycle(str, Enum):
    NotDefined = "notDefined",
    NotGoverned = "notGoverned",
    Governed = "governed",
    UnknownFutureValue = "unknownFutureValue",

