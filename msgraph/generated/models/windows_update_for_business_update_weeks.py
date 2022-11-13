from enum import Enum

class WindowsUpdateForBusinessUpdateWeeks(Enum):
    # Allow the user to set.
    UserDefined = "userDefined",
    # Scheduled the update installation on the first week of the month
    FirstWeek = "firstWeek",
    # Scheduled the update installation on the second week of the month
    SecondWeek = "secondWeek",
    # Scheduled the update installation on the third week of the month
    ThirdWeek = "thirdWeek",
    # Scheduled the update installation on the fourth week of the month
    FourthWeek = "fourthWeek",
    # Scheduled the update installation on every week of the month
    EveryWeek = "everyWeek",
    # Evolvable enum member
    UnknownFutureValue = "unknownFutureValue",

