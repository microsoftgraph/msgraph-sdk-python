from enum import Enum

class RuleOperation(str, Enum):
    Null = "null",
    Equals = "equals",
    NotEquals = "notEquals",
    Contains = "contains",
    NotContains = "notContains",
    LessThan = "lessThan",
    GreaterThan = "greaterThan",
    StartsWith = "startsWith",
    UnknownFutureValue = "unknownFutureValue",

