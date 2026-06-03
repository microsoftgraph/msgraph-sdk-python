from enum import Enum

class ApplicationDataType(str, Enum):
    None_ = "none",
    CodingFiles = "codingFiles",
    CreditCards = "creditCards",
    DatabaseFiles = "databaseFiles",
    Documents = "documents",
    MediaFiles = "mediaFiles",
    UnknownFutureValue = "unknownFutureValue",

