from enum import Enum

class BaselineParameterType(str, Enum):
    String = "string",
    Integer = "integer",
    Boolean = "boolean",
    # A marker value for members added after the release of this API.
    UnknownFutureValue = "unknownFutureValue",

