from enum import Enum

class AttributeMappingSourceType(str, Enum):
    Attribute = "Attribute",
    Constant = "Constant",
    Function = "Function",

