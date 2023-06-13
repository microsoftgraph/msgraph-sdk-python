from enum import Enum

class RunAsAccountType(str, Enum):
    # System context
    System = "system",
    # User context
    User = "user",

