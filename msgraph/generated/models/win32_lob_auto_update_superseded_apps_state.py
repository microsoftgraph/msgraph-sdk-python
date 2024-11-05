from enum import Enum

class Win32LobAutoUpdateSupersededAppsState(str, Enum):
    # Indicates that the auto-update superseded apps state is not configured and the app will not auto-update the superseded apps.
    NotConfigured = "notConfigured",
    # Indicates that the auto-update superseded apps state is enabled and the app will auto-update the superseded apps if the superseded apps are installed on the device.
    Enabled = "enabled",
    # Evolvable enumeration sentinel value. Do not use.
    UnknownFutureValue = "unknownFutureValue",

