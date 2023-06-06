from enum import Enum

class X509CertificateAuthenticationMode(str, Enum):
    X509CertificateSingleFactor = "x509CertificateSingleFactor",
    X509CertificateMultiFactor = "x509CertificateMultiFactor",
    UnknownFutureValue = "unknownFutureValue",

