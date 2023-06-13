from enum import Enum

class ServiceHealthClassificationType(str, Enum):
    Advisory = "advisory",
    Incident = "incident",
    UnknownFutureValue = "unknownFutureValue",

