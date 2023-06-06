from enum import Enum

class ExpirationPatternType(str, Enum):
    NotSpecified = "notSpecified",
    NoExpiration = "noExpiration",
    AfterDateTime = "afterDateTime",
    AfterDuration = "afterDuration",

