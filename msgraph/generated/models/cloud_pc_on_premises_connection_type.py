from enum import Enum

class CloudPcOnPremisesConnectionType(str, Enum):
    HybridAzureADJoin = "hybridAzureADJoin",
    AzureADJoin = "azureADJoin",
    UnknownFutureValue = "unknownFutureValue",

