from enum import Enum

class SharingCapabilities(str, Enum):
    Disabled = "disabled",
    ExternalUserSharingOnly = "externalUserSharingOnly",
    ExternalUserAndGuestSharing = "externalUserAndGuestSharing",
    ExistingExternalUserSharingOnly = "existingExternalUserSharingOnly",
    UnknownFutureValue = "unknownFutureValue",

