from enum import Enum

class Enablement(str, Enum):
    # Device default value, no intent.
    NotConfigured = "notConfigured",
    # Enables the setting on the device.
    Enabled = "enabled",
    # Disables the setting on the device.
    Disabled = "disabled",

