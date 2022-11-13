from enum import Enum

class SimulationStatus(Enum):
    Unknown = "unknown",
    Draft = "draft",
    Running = "running",
    Scheduled = "scheduled",
    Succeeded = "succeeded",
    Failed = "failed",
    Cancelled = "cancelled",
    Excluded = "excluded",
    UnknownFutureValue = "unknownFutureValue",

