from enum import Enum

class SimulationAutomationStatus(Enum):
    Unknown = "unknown",
    Draft = "draft",
    NotRunning = "notRunning",
    Running = "running",
    Completed = "completed",
    UnknownFutureValue = "unknownFutureValue",

