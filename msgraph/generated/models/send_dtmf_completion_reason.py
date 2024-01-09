from enum import Enum

class SendDtmfCompletionReason(str, Enum):
    Unknown = "unknown",
    CompletedSuccessfully = "completedSuccessfully",
    MediaOperationCanceled = "mediaOperationCanceled",
    UnknownFutureValue = "unknownFutureValue",

