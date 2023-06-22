from enum import Enum

class AttributeDefinitionMetadata(str, Enum):
    BaseAttributeName = "BaseAttributeName",
    ComplexObjectDefinition = "ComplexObjectDefinition",
    IsContainer = "IsContainer",
    IsCustomerDefined = "IsCustomerDefined",
    IsDomainQualified = "IsDomainQualified",
    LinkPropertyNames = "LinkPropertyNames",
    LinkTypeName = "LinkTypeName",
    MaximumLength = "MaximumLength",
    ReferencedProperty = "ReferencedProperty",

