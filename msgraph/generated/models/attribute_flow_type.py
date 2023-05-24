from enum import Enum

class AttributeFlowType(Enum):
    Always = "Always",
    ObjectAddOnly = "ObjectAddOnly",
    MultiValueAddOnly = "MultiValueAddOnly",
    ValueAddOnly = "ValueAddOnly",
    AttributeAddOnly = "AttributeAddOnly",

