from enum import Enum

class SimulationContentSource(str, Enum):
    Unknown = "unknown",
    Global_ = "global",
    Tenant = "tenant",
    UnknownFutureValue = "unknownFutureValue",

