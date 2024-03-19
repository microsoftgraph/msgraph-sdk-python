from enum import Enum

class CloudPcOnPremisesConnectionStatus(str, Enum):
    Pending = "pending",
    Running = "running",
    Passed = "passed",
    Failed = "failed",
    Warning = "warning",
    Informational = "informational",
    UnknownFutureValue = "unknownFutureValue",

