from enum import Enum

class BookingType(str, Enum):
    Unknown = "unknown",
    Standard = "standard",
    Reserved = "reserved",

