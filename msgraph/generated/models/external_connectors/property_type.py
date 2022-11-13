from enum import Enum

class PropertyType(Enum):
    String = "string",
    Int64 = "int64",
    Double = "double",
    DateTime = "dateTime",
    Boolean = "boolean",
    StringCollection = "stringCollection",
    Int64Collection = "int64Collection",
    DoubleCollection = "doubleCollection",
    DateTimeCollection = "dateTimeCollection",
    UnknownFutureValue = "unknownFutureValue",

