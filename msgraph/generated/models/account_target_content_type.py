from enum import Enum

class AccountTargetContentType(str, Enum):
    Unknown = "unknown",
    IncludeAll = "includeAll",
    AddressBook = "addressBook",
    UnknownFutureValue = "unknownFutureValue",

