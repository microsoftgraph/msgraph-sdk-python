from enum import Enum

class PlaceFeatureEnablement(str, Enum):
    Unknown = "unknown",
    Enabled = "enabled",
    Disabled = "disabled",
    UnknownFutureValue = "unknownFutureValue",

