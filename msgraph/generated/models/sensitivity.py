from enum import Enum

class Sensitivity(str, Enum):
    Normal = "normal",
    Personal = "personal",
    Private = "private",
    Confidential = "confidential",

