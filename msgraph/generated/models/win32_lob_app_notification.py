from enum import Enum

class Win32LobAppNotification(Enum):
    # Show all notifications.
    ShowAll = "showAll",
    # Only show restart notification and suppress other notifications.
    ShowReboot = "showReboot",
    # Hide all notifications.
    HideAll = "hideAll",

