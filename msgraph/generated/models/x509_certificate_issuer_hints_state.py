from enum import Enum

class X509CertificateIssuerHintsState(str, Enum):
    Disabled = "disabled",
    Enabled = "enabled",
    UnknownFutureValue = "unknownFutureValue",

