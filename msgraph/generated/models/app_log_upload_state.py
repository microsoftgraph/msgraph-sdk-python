from enum import Enum

class AppLogUploadState(str, Enum):
    # Default. Indicates that request is waiting to be processed or under processing.
    Pending = "pending",
    # Indicates that request is completed with file uploaded to Azure blob for download.
    Completed = "completed",
    # Indicates that request is completed with file uploaded to Azure blob for download.
    Failed = "failed",
    # Evolvable enumeration sentinel value. Do not use.
    UnknownFutureValue = "unknownFutureValue",

