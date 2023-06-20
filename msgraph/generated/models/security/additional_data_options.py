from enum import Enum

class AdditionalDataOptions(str, Enum):
    AllVersions = "allVersions",
    LinkedFiles = "linkedFiles",
    UnknownFutureValue = "unknownFutureValue",

