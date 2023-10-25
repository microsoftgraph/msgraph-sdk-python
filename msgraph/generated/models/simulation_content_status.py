from enum import Enum

class SimulationContentStatus(str, Enum):
    Unknown = "unknown",
    Draft = "draft",
    Ready = "ready",
    Archive = "archive",
    Delete = "delete",
    UnknownFutureValue = "unknownFutureValue",

