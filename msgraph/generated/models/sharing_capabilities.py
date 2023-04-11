from enum import Enum

class SharingCapabilities(Enum):
    Disabled = "disabled",
    ExternalUserSharingOnly = "externalUserSharingOnly",
    ExternalUserAndGuestSharing = "externalUserAndGuestSharing",
    ExistingExternalUserSharingOnly = "existingExternalUserSharingOnly",
    UnknownFutureValue = "unknownFutureValue",

