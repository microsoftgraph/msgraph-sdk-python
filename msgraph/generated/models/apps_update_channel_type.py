from enum import Enum

class AppsUpdateChannelType(str, Enum):
    Current = "current",
    MonthlyEnterprise = "monthlyEnterprise",
    SemiAnnual = "semiAnnual",
    UnknownFutureValue = "unknownFutureValue",

