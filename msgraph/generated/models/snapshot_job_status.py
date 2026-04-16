from enum import Enum

class SnapshotJobStatus(str, Enum):
    NotStarted = "notStarted",
    Running = "running",
    Succeeded = "succeeded",
    Failed = "failed",
    PartiallySuccessful = "partiallySuccessful",
    # A marker value for members added after the release of this API.
    UnknownFutureValue = "unknownFutureValue",

