from enum import Enum

class DirectoryDefinitionDiscoverabilities(Enum):
    None_ = "None",
    AttributeNames = "AttributeNames",
    AttributeDataTypes = "AttributeDataTypes",
    AttributeReadOnly = "AttributeReadOnly",
    ReferenceAttributes = "ReferenceAttributes",
    UnknownFutureValue = "UnknownFutureValue",

