from enum import Enum

class DirectoryDefinitionDiscoverabilities(str, Enum):
    None_ = "None",
    AttributeNames = "AttributeNames",
    AttributeDataTypes = "AttributeDataTypes",
    AttributeReadOnly = "AttributeReadOnly",
    ReferenceAttributes = "ReferenceAttributes",
    UnknownFutureValue = "UnknownFutureValue",

