from enum import Enum

class CaseOperationStatus(Enum):
    NotStarted = "notStarted",
    SubmissionFailed = "submissionFailed",
    Running = "running",
    Succeeded = "succeeded",
    PartiallySucceeded = "partiallySucceeded",
    Failed = "failed",
    UnknownFutureValue = "unknownFutureValue",

