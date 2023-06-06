from enum import Enum

class MdmAuthority(str, Enum):
    # Unknown
    Unknown = "unknown",
    # Intune
    Intune = "intune",
    # SCCM
    Sccm = "sccm",
    # Office365
    Office365 = "office365",

