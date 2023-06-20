from enum import Enum

class AttendeeType(str, Enum):
    Required = "required",
    Optional = "optional",
    Resource = "resource",

