from enum import Enum

class CustomExtensionResourceType(str, Enum):
    EntraRoles = "entraRoles",
    AzureResources = "azureResources",
    EntraGroups = "entraGroups",
    UnknownFutureValue = "unknownFutureValue",

