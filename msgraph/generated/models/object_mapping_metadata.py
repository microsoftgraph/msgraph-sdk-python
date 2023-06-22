from enum import Enum

class ObjectMappingMetadata(str, Enum):
    EscrowBehavior = "EscrowBehavior",
    DisableMonitoringForChanges = "DisableMonitoringForChanges",
    OriginalJoiningProperty = "OriginalJoiningProperty",
    Disposition = "Disposition",
    IsCustomerDefined = "IsCustomerDefined",
    ExcludeFromReporting = "ExcludeFromReporting",
    Unsynchronized = "Unsynchronized",

