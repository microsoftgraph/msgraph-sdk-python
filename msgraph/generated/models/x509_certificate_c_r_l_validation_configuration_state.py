from enum import Enum

class X509CertificateCRLValidationConfigurationState(str, Enum):
    Disabled = "disabled",
    Enabled = "enabled",
    UnknownFutureValue = "unknownFutureValue",

