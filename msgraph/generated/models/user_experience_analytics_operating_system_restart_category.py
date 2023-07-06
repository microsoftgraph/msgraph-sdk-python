from enum import Enum

class UserExperienceAnalyticsOperatingSystemRestartCategory(str, Enum):
    # Default. Set to unknown if device operating system restart category has not yet been calculated.
    Unknown = "unknown",
    # Indicates that the device operating system restart is along with an update.
    RestartWithUpdate = "restartWithUpdate",
    # Indicates that the device operating system restart is without update.
    RestartWithoutUpdate = "restartWithoutUpdate",
    # Indicates that the device operating system restart is due to a specific stop error.
    BlueScreen = "blueScreen",
    # Indicates that the device operating system restart is due to shutdown with update.
    ShutdownWithUpdate = "shutdownWithUpdate",
    # Indicates that the device operating system restart is due to shutdown without update.
    ShutdownWithoutUpdate = "shutdownWithoutUpdate",
    # Indicates that the device operating system restart is due to update long power-button press.
    LongPowerButtonPress = "longPowerButtonPress",
    # Indicates that the device operating system restart is due to boot error.
    BootError = "bootError",
    # Indicates that the device operating system restarted after an update.
    Update = "update",
    # Evolvable enumeration sentinel value. Do not use.
    UnknownFutureValue = "unknownFutureValue",

