from enum import Enum

class LobbyBypassScope(str, Enum):
    Organizer = "organizer",
    Organization = "organization",
    OrganizationAndFederated = "organizationAndFederated",
    Everyone = "everyone",
    UnknownFutureValue = "unknownFutureValue",
    Invited = "invited",
    OrganizationExcludingGuests = "organizationExcludingGuests",

