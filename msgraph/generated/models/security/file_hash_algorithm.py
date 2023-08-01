from enum import Enum

class FileHashAlgorithm(str, Enum):
    Unknown = "unknown",
    Md5 = "md5",
    Sha1 = "sha1",
    Sha256 = "sha256",
    Sha256ac = "sha256ac",
    UnknownFutureValue = "unknownFutureValue",

