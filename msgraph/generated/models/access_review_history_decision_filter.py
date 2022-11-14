from enum import Enum

class AccessReviewHistoryDecisionFilter(Enum):
    Approve = "approve",
    Deny = "deny",
    NotReviewed = "notReviewed",
    DontKnow = "dontKnow",
    NotNotified = "notNotified",
    UnknownFutureValue = "unknownFutureValue",

