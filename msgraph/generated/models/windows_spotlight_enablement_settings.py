from enum import Enum

class WindowsSpotlightEnablementSettings(Enum):
    # Spotlight on lock screen is not configured
    NotConfigured = "notConfigured",
    # Disable Windows Spotlight on lock screen
    Disabled = "disabled",
    # Enable Windows Spotlight on lock screen
    Enabled = "enabled",

