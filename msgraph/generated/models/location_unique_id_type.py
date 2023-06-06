from enum import Enum

class LocationUniqueIdType(str, Enum):
    Unknown = "unknown",
    LocationStore = "locationStore",
    Directory = "directory",
    Private = "private",
    Bing = "bing",

