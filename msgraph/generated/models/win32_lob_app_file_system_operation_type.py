from enum import Enum

class Win32LobAppFileSystemOperationType(str, Enum):
    # Not configured.
    NotConfigured = "notConfigured",
    # Whether the specified file or folder exists.
    Exists = "exists",
    # Last modified date.
    ModifiedDate = "modifiedDate",
    # Created date.
    CreatedDate = "createdDate",
    # Version value type.
    Version = "version",
    # Size detection type.
    SizeInMB = "sizeInMB",

