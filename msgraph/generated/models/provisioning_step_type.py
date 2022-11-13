from enum import Enum

class ProvisioningStepType(Enum):
    Import_escaped = "import",
    Scoping = "scoping",
    Matching = "matching",
    Processing = "processing",
    ReferenceResolution = "referenceResolution",
    Export = "export",
    UnknownFutureValue = "unknownFutureValue",

