from enum import Enum

class WeeklySchedule(str, Enum):
    # User Defined, default value, no intent.
    UserDefined = "userDefined",
    # Everyday.
    Everyday = "everyday",
    # Sunday.
    Sunday = "sunday",
    # Monday.
    Monday = "monday",
    # Tuesday.
    Tuesday = "tuesday",
    # Wednesday.
    Wednesday = "wednesday",
    # Thursday.
    Thursday = "thursday",
    # Friday.
    Friday = "friday",
    # Saturday.
    Saturday = "saturday",

