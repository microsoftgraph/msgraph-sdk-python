from enum import Enum

class ServiceHealthClassificationType(Enum):
    Advisory = "advisory",
    Incident = "incident",
    UnknownFutureValue = "unknownFutureValue",

