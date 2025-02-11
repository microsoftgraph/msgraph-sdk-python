from enum import Enum

class AllowedLobbyAdmitterRoles(str, Enum):
    OrganizerAndCoOrganizersAndPresenters = "organizerAndCoOrganizersAndPresenters",
    OrganizerAndCoOrganizers = "organizerAndCoOrganizers",
    UnknownFutureValue = "unknownFutureValue",

