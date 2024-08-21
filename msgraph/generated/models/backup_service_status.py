from enum import Enum

class BackupServiceStatus(str, Enum):
    Disabled = "disabled",
    Enabled = "enabled",
    ProtectionChangeLocked = "protectionChangeLocked",
    RestoreLocked = "restoreLocked",
    UnknownFutureValue = "unknownFutureValue",

