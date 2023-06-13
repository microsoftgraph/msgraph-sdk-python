from enum import Enum

class ThreatAssessmentStatus(str, Enum):
    Pending = "pending",
    Completed = "completed",

