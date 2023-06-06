from enum import Enum

class Win32LobAppRuleOperator(str, Enum):
    # Not configured.
    NotConfigured = "notConfigured",
    # Equal operator.
    Equal = "equal",
    # Not equal operator.
    NotEqual = "notEqual",
    # Greater than operator.
    GreaterThan = "greaterThan",
    # Greater than or equal operator.
    GreaterThanOrEqual = "greaterThanOrEqual",
    # Less than operator.
    LessThan = "lessThan",
    # Less than or equal operator.
    LessThanOrEqual = "lessThanOrEqual",

