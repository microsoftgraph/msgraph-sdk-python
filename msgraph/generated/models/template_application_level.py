from enum import Enum

class TemplateApplicationLevel(str, Enum):
    None_ = "none",
    NewPartners = "newPartners",
    ExistingPartners = "existingPartners",
    UnknownFutureValue = "unknownFutureValue",

