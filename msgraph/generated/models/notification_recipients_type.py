from enum import Enum

class NotificationRecipientsType(str, Enum):
    None_ = "none",
    GlobalAdmins = "globalAdmins",
    BackupAdmins = "backupAdmins",
    Custom = "custom",
    AllAdmins = "allAdmins",
    UnknownFutureValue = "unknownFutureValue",

