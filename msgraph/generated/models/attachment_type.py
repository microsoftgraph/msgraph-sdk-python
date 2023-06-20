from enum import Enum

class AttachmentType(str, Enum):
    File = "file",
    Item = "item",
    Reference = "reference",

