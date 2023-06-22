from enum import Enum

class ThreatExpectedAssessment(str, Enum):
    Block = "block",
    Unblock = "unblock",

