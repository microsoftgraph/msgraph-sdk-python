from enum import Enum

class WindowsHelloForBusinessPinUsage(Enum):
    # Allowed the usage of certain pin rule
    Allowed = "allowed",
    # Enforce the usage of certain pin rule
    Required = "required",
    # Forbit the usage of certain pin rule
    Disallowed = "disallowed",

