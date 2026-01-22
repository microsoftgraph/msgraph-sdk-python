from enum import Enum

class ServiceStatus(str, Enum):
    Stopped = "stopped",
    Starting = "starting",
    Running = "running",
    Disabled = "disabled",
    Onboarding = "onboarding",
    Unknown = "unknown",
    UnknownFutureValue = "unknownFutureValue",

