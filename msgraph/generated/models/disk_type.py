from enum import Enum

class DiskType(Enum):
    # Enum member for unknown or default diskType
    Unknown = "unknown",
    # Enum member for HDD devices
    Hdd = "hdd",
    # Enum member for SSD devices
    Ssd = "ssd",
    # Evolvable enum member
    UnknownFutureValue = "unknownFutureValue",

