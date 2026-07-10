from enum import Enum

class RecoveryAction(str, Enum):
    # Represents a soft delete action during recovery
    SoftDelete = "softDelete",
    # Represents an update action during recovery
    Update = "update",
    # Represents a restore action during recovery
    Restore = "restore",
    # This will help in making this enum evolable and adding more values in the future
    UnknownFutureValue = "unknownFutureValue",

