from enum import Enum

class DeviceManagementExchangeConnectorStatus(str, Enum):
    # No Connector exists.
    None_ = "none",
    # Pending Connection to the Exchange Environment.
    ConnectionPending = "connectionPending",
    # Connected to the Exchange Environment
    Connected = "connected",
    # Disconnected from the Exchange Environment
    Disconnected = "disconnected",
    # Evolvable enumeration sentinel value. Do not use.
    UnknownFutureValue = "unknownFutureValue",

