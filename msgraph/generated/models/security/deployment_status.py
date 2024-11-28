from enum import Enum

class DeploymentStatus(str, Enum):
    UpToDate = "upToDate",
    Outdated = "outdated",
    Updating = "updating",
    UpdateFailed = "updateFailed",
    NotConfigured = "notConfigured",
    Unreachable = "unreachable",
    Disconnected = "disconnected",
    StartFailure = "startFailure",
    Syncing = "syncing",
    UnknownFutureValue = "unknownFutureValue",

