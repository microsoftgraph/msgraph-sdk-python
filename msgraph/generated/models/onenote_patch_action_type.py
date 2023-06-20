from enum import Enum

class OnenotePatchActionType(str, Enum):
    Replace = "Replace",
    Append = "Append",
    Delete = "Delete",
    Insert = "Insert",
    Prepend = "Prepend",

