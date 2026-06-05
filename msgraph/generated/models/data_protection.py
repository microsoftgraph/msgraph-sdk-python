from enum import Enum

class DataProtection(str, Enum):
    None_ = "none",
    ImpactAssessments = "impactAssessments",
    Officers = "officers",
    SecureCrossBorderDataTransfer = "secureCrossBorderDataTransfer",
    UnknownFutureValue = "unknownFutureValue",

