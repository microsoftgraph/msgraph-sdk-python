from enum import Enum

class FileStorageContainerBillingClassification(str, Enum):
    Standard = "standard",
    Trial = "trial",
    DirectToCustomer = "directToCustomer",
    UnknownFutureValue = "unknownFutureValue",

