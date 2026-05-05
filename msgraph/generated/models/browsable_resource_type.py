from enum import Enum

class BrowsableResourceType(str, Enum):
    None_ = "none",
    Site = "site",
    DocumentLibrary = "documentLibrary",
    Folder = "folder",
    UnknownFutureValue = "unknownFutureValue",

