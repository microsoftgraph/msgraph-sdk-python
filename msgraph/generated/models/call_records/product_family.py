from enum import Enum

class ProductFamily(str, Enum):
    Unknown = "unknown",
    Teams = "teams",
    SkypeForBusiness = "skypeForBusiness",
    Lync = "lync",
    UnknownFutureValue = "unknownFutureValue",
    AzureCommunicationServices = "azureCommunicationServices",

