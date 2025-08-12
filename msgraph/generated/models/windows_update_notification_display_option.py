from enum import Enum

class WindowsUpdateNotificationDisplayOption(str, Enum):
    # Not configured
    NotConfigured = "notConfigured",
    # Use the default Windows Update notifications.
    DefaultNotifications = "defaultNotifications",
    # Turn off all notifications, excluding restart warnings.
    RestartWarningsOnly = "restartWarningsOnly",
    # Turn off all notifications, including restart warnings.
    DisableAllNotifications = "disableAllNotifications",
    # Evolvable enumeration sentinel value. Do not use.
    UnknownFutureValue = "unknownFutureValue",

