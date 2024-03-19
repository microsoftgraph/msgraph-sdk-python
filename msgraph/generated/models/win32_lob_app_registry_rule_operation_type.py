from enum import Enum

class Win32LobAppRegistryRuleOperationType(str, Enum):
    # Default. Indicates that the rule does not have the operation type configured.
    NotConfigured = "notConfigured",
    # Indicates that the rule evaluates whether the specified registry key or value exists.
    Exists = "exists",
    # Indicates that the rule evaluates whether the specified registry key or value does not exist. It is the functional inverse of an equivalent rule that uses operation type `exists`.
    DoesNotExist = "doesNotExist",
    # Indicates that the rule compares the value read at the given registry value against a provided comparison value by string comparison.
    String = "string",
    # Indicates that the rule compares the value read at the given registry value against a provided comparison value by integer comparison.
    Integer = "integer",
    # Indicates that the rule compares the value read at the given registry value against a provided comparison value via version semantics (both operand values will be parsed as versions and directly compared). If the value read at the given registry value is not discovered to be in version-compatible format, a string comparison will be used instead.
    Version = "version",

