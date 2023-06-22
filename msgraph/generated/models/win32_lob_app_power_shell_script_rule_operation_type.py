from enum import Enum

class Win32LobAppPowerShellScriptRuleOperationType(str, Enum):
    # Not configured.
    NotConfigured = "notConfigured",
    # Output data type is string.
    String = "string",
    # Output data type is date time.
    DateTime = "dateTime",
    # Output data type is integer.
    Integer = "integer",
    # Output data type is float.
    Float = "float",
    # Output data type is version.
    Version = "version",
    # Output data type is boolean.
    Boolean = "boolean",

