from enum import Enum

class AttributeFlowBehavior(str, Enum):
    FlowWhenChanged = "FlowWhenChanged",
    FlowAlways = "FlowAlways",

