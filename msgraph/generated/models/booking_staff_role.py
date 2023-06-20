from enum import Enum

class BookingStaffRole(str, Enum):
    Guest = "guest",
    Administrator = "administrator",
    Viewer = "viewer",
    ExternalGuest = "externalGuest",
    UnknownFutureValue = "unknownFutureValue",
    Scheduler = "scheduler",
    TeamMember = "teamMember",

