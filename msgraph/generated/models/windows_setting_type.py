from enum import Enum

class WindowsSettingType(str, Enum):
    Roaming = "roaming",
    Backup = "backup",
    UnknownFutureValue = "unknownFutureValue",

