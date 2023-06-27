from enum import Enum

class ValueType(str, Enum):
    Enum = "enum",
    String = "string",
    Int = "int",
    Bool = "bool",
    UnknownFutureValue = "unknownFutureValue",

