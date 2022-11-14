from enum import Enum

class MobileAppContentFileUploadState(Enum):
    Success = "success",
    TransientError = "transientError",
    Error = "error",
    Unknown = "unknown",
    AzureStorageUriRequestSuccess = "azureStorageUriRequestSuccess",
    AzureStorageUriRequestPending = "azureStorageUriRequestPending",
    AzureStorageUriRequestFailed = "azureStorageUriRequestFailed",
    AzureStorageUriRequestTimedOut = "azureStorageUriRequestTimedOut",
    AzureStorageUriRenewalSuccess = "azureStorageUriRenewalSuccess",
    AzureStorageUriRenewalPending = "azureStorageUriRenewalPending",
    AzureStorageUriRenewalFailed = "azureStorageUriRenewalFailed",
    AzureStorageUriRenewalTimedOut = "azureStorageUriRenewalTimedOut",
    CommitFileSuccess = "commitFileSuccess",
    CommitFilePending = "commitFilePending",
    CommitFileFailed = "commitFileFailed",
    CommitFileTimedOut = "commitFileTimedOut",

