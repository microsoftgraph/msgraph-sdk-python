from enum import Enum

class RestEncryptionType(str, Enum):
    None_ = "none",
    Aes = "aes",
    Bitlocker = "bitlocker",
    Blowfish = "blowfish",
    Des = "des",
    Rc4 = "rc4",
    Rsa = "rsa",
    NotSupported = "notSupported",
    UnknownFutureValue = "unknownFutureValue",

