from enum import Enum

class AuthenticationStrengthPolicyType(str, Enum):
    BuiltIn = "builtIn",
    Custom = "custom",
    UnknownFutureValue = "unknownFutureValue",

