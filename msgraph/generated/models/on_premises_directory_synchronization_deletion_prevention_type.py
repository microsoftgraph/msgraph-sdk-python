from enum import Enum

class OnPremisesDirectorySynchronizationDeletionPreventionType(str, Enum):
    Disabled = "disabled",
    EnabledForCount = "enabledForCount",
    EnabledForPercentage = "enabledForPercentage",
    UnknownFutureValue = "unknownFutureValue",

