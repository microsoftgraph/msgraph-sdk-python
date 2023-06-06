from enum import Enum

class EducationFeedbackResourceOutcomeStatus(str, Enum):
    NotPublished = "notPublished",
    PendingPublish = "pendingPublish",
    Published = "published",
    FailedPublish = "failedPublish",
    UnknownFutureValue = "unknownFutureValue",

