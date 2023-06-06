from enum import Enum

class GroupType(str, Enum):
    UnifiedGroups = "unifiedGroups",
    AzureAD = "azureAD",
    UnknownFutureValue = "unknownFutureValue",

