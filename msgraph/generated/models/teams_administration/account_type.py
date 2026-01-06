from enum import Enum

class AccountType(str, Enum):
    User = "user",
    ResourceAccount = "resourceAccount",
    Guest = "guest",
    SfbOnPremUser = "sfbOnPremUser",
    Unknown = "unknown",
    UnknownFutureValue = "unknownFutureValue",
    IneligibleUser = "ineligibleUser",

