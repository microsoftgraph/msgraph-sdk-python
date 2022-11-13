from enum import Enum

class X509CertificateRuleType(Enum):
    IssuerSubject = "issuerSubject",
    PolicyOID = "policyOID",
    UnknownFutureValue = "unknownFutureValue",

