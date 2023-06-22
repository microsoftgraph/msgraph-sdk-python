from enum import Enum

class DeviceComplianceActionType(str, Enum):
    # No Action
    NoAction = "noAction",
    # Send Notification
    Notification = "notification",
    # Block the device in AAD
    Block = "block",
    # Retire the device
    Retire = "retire",
    # Wipe the device
    Wipe = "wipe",
    # Remove Resource Access Profiles from the device
    RemoveResourceAccessProfiles = "removeResourceAccessProfiles",
    # Send push notification to device
    PushNotification = "pushNotification",

