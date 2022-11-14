from enum import Enum

class ExpirationPatternType(Enum):
    NotSpecified = "notSpecified",
    NoExpiration = "noExpiration",
    AfterDateTime = "afterDateTime",
    AfterDuration = "afterDuration",

