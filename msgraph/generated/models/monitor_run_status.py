from enum import Enum

class MonitorRunStatus(str, Enum):
    Successful = "successful",
    PartiallySuccessful = "partiallySuccessful",
    Failed = "failed",
    # A marker value for members added after the release of this API.
    UnknownFutureValue = "unknownFutureValue",

