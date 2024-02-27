from enum import Enum

class MultiFactorAuthConfiguration(str, Enum):
    NotRequired = "notRequired",
    Required = "required",
    UnknownFutureValue = "unknownFutureValue",

