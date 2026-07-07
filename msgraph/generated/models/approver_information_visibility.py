from enum import Enum

class ApproverInformationVisibility(str, Enum):
    Default = "default",
    NotVisible = "notVisible",
    Visible = "visible",
    UnknownFutureValue = "unknownFutureValue",

