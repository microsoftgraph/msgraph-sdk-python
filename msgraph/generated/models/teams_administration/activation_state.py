from enum import Enum

class ActivationState(str, Enum):
    Activated = "activated",
    AssignmentPending = "assignmentPending",
    AssignmentFailed = "assignmentFailed",
    UpdatePending = "updatePending",
    UpdateFailed = "updateFailed",
    UnknownFutureValue = "unknownFutureValue",

