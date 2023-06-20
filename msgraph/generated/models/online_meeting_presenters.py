from enum import Enum

class OnlineMeetingPresenters(str, Enum):
    Everyone = "everyone",
    Organization = "organization",
    RoleIsPresenter = "roleIsPresenter",
    Organizer = "organizer",
    UnknownFutureValue = "unknownFutureValue",

