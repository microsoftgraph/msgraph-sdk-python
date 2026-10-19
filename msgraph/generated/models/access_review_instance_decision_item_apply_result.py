from enum import Enum

class AccessReviewInstanceDecisionItemApplyResult(str, Enum):
    New = "new",
    AppliedSuccessfully = "appliedSuccessfully",
    AppliedWithUnknownFailure = "appliedWithUnknownFailure",
    AppliedSuccessfullyButObjectNotFound = "appliedSuccessfullyButObjectNotFound",
    ApplyNotSupported = "applyNotSupported",
    UnknownFutureValue = "unknownFutureValue",

