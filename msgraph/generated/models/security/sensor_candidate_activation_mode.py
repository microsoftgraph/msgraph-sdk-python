from enum import Enum

class SensorCandidateActivationMode(str, Enum):
    Manual = "manual",
    Automated = "automated",
    UnknownFutureValue = "unknownFutureValue",

