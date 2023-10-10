from enum import Enum

class Label(str, Enum):
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
    IconUrl = "iconUrl",

