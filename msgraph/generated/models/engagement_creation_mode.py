from enum import Enum

class EngagementCreationMode(str, Enum):
    # Unspecified creation mode.
    None_ = "none",
    # Creation is a migration.
    Migration = "migration",
    # A marker value for members added after the release of this API.
    UnknownFutureValue = "unknownFutureValue",

