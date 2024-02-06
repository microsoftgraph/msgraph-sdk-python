from enum import Enum

class BillingPeriod(str, Enum):
    Current = "current",
    Last = "last",
    UnknownFutureValue = "unknownFutureValue",

