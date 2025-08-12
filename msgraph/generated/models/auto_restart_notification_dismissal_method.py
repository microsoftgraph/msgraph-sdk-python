from enum import Enum

class AutoRestartNotificationDismissalMethod(str, Enum):
    # Not configured
    NotConfigured = "notConfigured",
    # Auto dismissal Indicates that the notification is automatically dismissed without user intervention
    Automatic = "automatic",
    # User dismissal. Allows the user to dismiss the notification
    User = "user",
    # Evolvable enumeration sentinel value. Do not use.
    UnknownFutureValue = "unknownFutureValue",

