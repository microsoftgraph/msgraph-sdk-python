from enum import Enum

class SharePointMigrationObjectType(str, Enum):
    Site = "site",
    Web = "web",
    Folder = "folder",
    List_ = "list",
    ListItem = "listItem",
    File = "file",
    Alert = "alert",
    SharedWithObject = "sharedWithObject",
    Invalid = "invalid",
    UnknownFutureValue = "unknownFutureValue",

