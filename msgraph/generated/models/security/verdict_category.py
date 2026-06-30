from enum import Enum

class VerdictCategory(str, Enum):
    None_ = "none",
    Malware = "malware",
    Phish = "phish",
    SiteUnavailable = "siteUnavailable",
    Spam = "spam",
    DecryptionFailed = "decryptionFailed",
    UnsupportedUriScheme = "unsupportedUriScheme",
    UnsupportedFileType = "unsupportedFileType",
    Undefined = "undefined",
    UnknownFutureValue = "unknownFutureValue",

