from enum import Enum

class TrainingAssignedTo(str, Enum):
    None_ = "none",
    AllUsers = "allUsers",
    ClickedPayload = "clickedPayload",
    Compromised = "compromised",
    ReportedPhish = "reportedPhish",
    ReadButNotClicked = "readButNotClicked",
    DidNothing = "didNothing",
    UnknownFutureValue = "unknownFutureValue",

