from enum import Enum

class SimulationAttackType(str, Enum):
    Unknown = "unknown",
    Social = "social",
    Cloud = "cloud",
    Endpoint = "endpoint",
    UnknownFutureValue = "unknownFutureValue",

