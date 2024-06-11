from enum import Enum

class WindowsUserType(str, Enum):
    # Indicates that the user has administrator privileges.
    Administrator = "administrator",
    # Indicates that the user is a low-rights user without administrator privileges.
    Standard = "standard",
    # Evolvable enumeration sentinel value. Do not use.
    UnknownFutureValue = "unknownFutureValue",

