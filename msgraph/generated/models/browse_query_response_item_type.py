from enum import Enum

class BrowseQueryResponseItemType(str, Enum):
    None_ = "none",
    Site = "site",
    DocumentLibrary = "documentLibrary",
    Folder = "folder",
    File = "file",
    UnknownFutureValue = "unknownFutureValue",

