from enum import Enum

class MdmAuthority(Enum):
    # Unknown
    Unknown = "unknown",
    # Intune
    Intune = "intune",
    # SCCM
    Sccm = "sccm",
    # Office365
    Office365 = "office365",

