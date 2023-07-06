from enum import Enum

class AppLogDecryptionAlgorithm(str, Enum):
    # decrypting using Aes256.
    Aes256 = "aes256",
    # Evolvable enumeration sentinel value. Do not use.
    UnknownFutureValue = "unknownFutureValue",

