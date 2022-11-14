from enum import Enum

class DeviceManagementExchangeConnectorStatus(Enum):
    # No Connector exists.
    None_escaped = "none",
    # Pending Connection to the Exchange Environment.
    ConnectionPending = "connectionPending",
    # Connected to the Exchange Environment
    Connected = "connected",
    # Disconnected from the Exchange Environment
    Disconnected = "disconnected",

