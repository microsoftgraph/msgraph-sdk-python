from enum import Enum

class OnenoteUserRole(str, Enum):
    None_ = "None",
    Owner = "Owner",
    Contributor = "Contributor",
    Reader = "Reader",

