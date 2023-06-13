from enum import Enum

class IdentityUserFlowAttributeType(str, Enum):
    BuiltIn = "builtIn",
    Custom = "custom",
    Required = "required",
    UnknownFutureValue = "unknownFutureValue",

