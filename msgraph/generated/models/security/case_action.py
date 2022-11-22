from enum import Enum

class CaseAction(Enum):
    ContentExport = "contentExport",
    ApplyTags = "applyTags",
    ConvertToPdf = "convertToPdf",
    Index = "index",
    EstimateStatistics = "estimateStatistics",
    AddToReviewSet = "addToReviewSet",
    HoldUpdate = "holdUpdate",
    UnknownFutureValue = "unknownFutureValue",
    PurgeData = "purgeData",

