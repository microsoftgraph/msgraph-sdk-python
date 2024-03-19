from enum import Enum

class CloudPcDomainJoinType(str, Enum):
    AzureADJoin = "azureADJoin",
    HybridAzureADJoin = "hybridAzureADJoin",
    UnknownFutureValue = "unknownFutureValue",

