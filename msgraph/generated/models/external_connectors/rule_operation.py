from enum import Enum

class RuleOperation(Enum):
    Equals = "equals",
    NotEquals = "notEquals",
    Contains = "contains",
    NotContains = "notContains",
    LessThan = "lessThan",
    GreaterThan = "greaterThan",
    StartsWith = "startsWith",
    UnknownFutureValue = "unknownFutureValue",

