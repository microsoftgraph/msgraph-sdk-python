from enum import Enum

class SensorType(str, Enum):
    AdConnectIntegrated = "adConnectIntegrated",
    AdcsIntegrated = "adcsIntegrated",
    AdfsIntegrated = "adfsIntegrated",
    DomainControllerIntegrated = "domainControllerIntegrated",
    DomainControllerStandalone = "domainControllerStandalone",
    UnknownFutureValue = "unknownFutureValue",

