from enum import Enum

class ThreatAssessmentResultType(str, Enum):
    CheckPolicy = "checkPolicy",
    Rescan = "rescan",
    UnknownFutureValue = "unknownFutureValue",

