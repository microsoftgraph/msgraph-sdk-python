from enum import Enum

class CalendarSharingAction(str, Enum):
    Accept = "accept",
    AcceptAndViewCalendar = "acceptAndViewCalendar",
    ViewCalendar = "viewCalendar",
    AddThisCalendar = "addThisCalendar",

