from enum import Enum

class EnrollmentState(str, Enum):
    # Device enrollment state is unknown
    Unknown = "unknown",
    # Device is Enrolled.
    Enrolled = "enrolled",
    # Enrolled but it's enrolled via enrollment profile and the enrolled profile is different from the assigned profile.
    PendingReset = "pendingReset",
    # Not enrolled and there is enrollment failure record.
    Failed = "failed",
    # Device is imported but not enrolled.
    NotContacted = "notContacted",

