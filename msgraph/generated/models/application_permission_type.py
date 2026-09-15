from enum import Enum

class ApplicationPermissionType(str, Enum):
    # Represents a type of permission that is for an app only scenario. No user is involved.
    Role = "role",
    # Represents a type of permission that is for an app and user scenario.
    Scope = "scope",
    # This will help in making this enum evolable and adding more values in the future-
    UnknownFutureValue = "unknownFutureValue",

