from enum import Enum

class SimulationAutomationStatus(str, Enum):
    Unknown = "unknown",
    Draft = "draft",
    NotRunning = "notRunning",
    Running = "running",
    Completed = "completed",
    UnknownFutureValue = "unknownFutureValue",

