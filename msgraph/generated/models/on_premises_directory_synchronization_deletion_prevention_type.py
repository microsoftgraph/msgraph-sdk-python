from enum import Enum

class OnPremisesDirectorySynchronizationDeletionPreventionType(Enum):
    Disabled = "disabled",
    EnabledForCount = "enabledForCount",
    EnabledForPercentage = "enabledForPercentage",
    UnknownFutureValue = "unknownFutureValue",

