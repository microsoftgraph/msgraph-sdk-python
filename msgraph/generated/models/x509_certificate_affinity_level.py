from enum import Enum

class X509CertificateAffinityLevel(str, Enum):
    Low = "low",
    High = "high",
    UnknownFutureValue = "unknownFutureValue",

