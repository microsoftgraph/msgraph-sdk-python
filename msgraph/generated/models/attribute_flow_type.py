from enum import Enum

class AttributeFlowType(str, Enum):
    Always = "Always",
    ObjectAddOnly = "ObjectAddOnly",
    MultiValueAddOnly = "MultiValueAddOnly",
    ValueAddOnly = "ValueAddOnly",
    AttributeAddOnly = "AttributeAddOnly",

