from enum import Enum

class ExportOptions(str, Enum):
    OriginalFiles = "originalFiles",
    Text = "text",
    PdfReplacement = "pdfReplacement",
    Tags = "tags",
    UnknownFutureValue = "unknownFutureValue",

