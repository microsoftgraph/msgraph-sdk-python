from enum import Enum

class SettingSourceType(str, Enum):
    DeviceConfiguration = "deviceConfiguration",
    DeviceIntent = "deviceIntent",

