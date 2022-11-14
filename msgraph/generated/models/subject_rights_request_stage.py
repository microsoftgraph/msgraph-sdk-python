from enum import Enum

class SubjectRightsRequestStage(Enum):
    ContentRetrieval = "contentRetrieval",
    ContentReview = "contentReview",
    GenerateReport = "generateReport",
    ContentDeletion = "contentDeletion",
    CaseResolved = "caseResolved",
    ContentEstimate = "contentEstimate",
    UnknownFutureValue = "unknownFutureValue",

