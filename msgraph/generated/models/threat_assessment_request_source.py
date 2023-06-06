from enum import Enum

class ThreatAssessmentRequestSource(str, Enum):
    Undefined = "undefined",
    User = "user",
    Administrator = "administrator",

