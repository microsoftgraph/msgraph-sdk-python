from enum import Enum

class ArtifactRestoreStatus(str, Enum):
    Added = "added",
    Scheduling = "scheduling",
    Scheduled = "scheduled",
    InProgress = "inProgress",
    Succeeded = "succeeded",
    Failed = "failed",
    UnknownFutureValue = "unknownFutureValue",

