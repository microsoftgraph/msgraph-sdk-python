from enum import Enum

class AccessReviewHistoryDecisionFilter(str, Enum):
    Approve = "approve",
    Deny = "deny",
    NotReviewed = "notReviewed",
    DontKnow = "dontKnow",
    NotNotified = "notNotified",
    UnknownFutureValue = "unknownFutureValue",

