from enum import Enum

class DeviceManagementExchangeConnectorSyncType(Enum):
    # Discover all the device in Exchange.
    FullSync = "fullSync",
    # Discover only the device in Exchange which have updated during the delta sync window.
    DeltaSync = "deltaSync",

