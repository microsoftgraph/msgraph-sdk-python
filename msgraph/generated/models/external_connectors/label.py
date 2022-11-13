from enum import Enum

class Label(Enum):
    Title = "title",
    Url = "url",
    CreatedBy = "createdBy",
    LastModifiedBy = "lastModifiedBy",
    Authors = "authors",
    CreatedDateTime = "createdDateTime",
    LastModifiedDateTime = "lastModifiedDateTime",
    FileName = "fileName",
    FileExtension = "fileExtension",
    UnknownFutureValue = "unknownFutureValue",

