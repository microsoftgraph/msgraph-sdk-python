from enum import Enum

class Win32LobAppFileSystemOperationType(str, Enum):
    # Default. Indicates that the rule does not have the operation type configured.
    NotConfigured = "notConfigured",
    # Indicates that the rule evaluates whether the specified file or folder exists.
    Exists = "exists",
    # Indicates that the rule compares the modified date of the specified file against a provided comparison value by DateTime comparison.
    ModifiedDate = "modifiedDate",
    # Indicates that the rule compares the created date of the specified file against a provided comparison value by DateTime comparison.
    CreatedDate = "createdDate",
    # Indicates that the rule compares the detected version of the specified file against a provided comparison value via version semantics (both operand values will be parsed as versions and directly compared). If the value read at the given registry value is not discovered to be in version-compatible format, a string comparison will be used instead.
    Version = "version",
    # Indicates that the rule compares the size of the file in MiB (rounded down) against a provided comparison value by integer comparison.
    SizeInMB = "sizeInMB",

