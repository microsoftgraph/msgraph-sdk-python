from enum import Enum

class WelcomeScreenMeetingInformation(str, Enum):
    # User Defined, default value, no intent.
    UserDefined = "userDefined",
    # Show organizer and time only.
    ShowOrganizerAndTimeOnly = "showOrganizerAndTimeOnly",
    # Show organizer, time and subject (subject is hidden for private meetings).
    ShowOrganizerAndTimeAndSubject = "showOrganizerAndTimeAndSubject",

