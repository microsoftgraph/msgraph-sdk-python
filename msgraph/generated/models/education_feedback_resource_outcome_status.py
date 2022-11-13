from enum import Enum

class EducationFeedbackResourceOutcomeStatus(Enum):
    NotPublished = "notPublished",
    PendingPublish = "pendingPublish",
    Published = "published",
    FailedPublish = "failedPublish",
    UnknownFutureValue = "unknownFutureValue",

