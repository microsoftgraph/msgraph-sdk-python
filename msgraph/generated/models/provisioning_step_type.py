from enum import Enum

class ProvisioningStepType(Enum):
    Import_ = "import",
    Scoping = "scoping",
    Matching = "matching",
    Processing = "processing",
    ReferenceResolution = "referenceResolution",
    Export = "export",
    UnknownFutureValue = "unknownFutureValue",

