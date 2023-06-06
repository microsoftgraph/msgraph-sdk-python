from enum import Enum

class CertificateStatus(str, Enum):
    NotProvisioned = "notProvisioned",
    Provisioned = "provisioned",

