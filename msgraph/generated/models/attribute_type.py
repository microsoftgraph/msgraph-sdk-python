from enum import Enum

class AttributeType(str, Enum):
    String = "String",
    Integer = "Integer",
    Reference = "Reference",
    Binary = "Binary",
    Boolean = "Boolean",
    DateTime = "DateTime",

