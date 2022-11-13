from enum import Enum

class BitLockerEncryptionMethod(Enum):
    # AES-CBC 128-bit.
    AesCbc128 = "aesCbc128",
    # AES-CBC 256-bit.
    AesCbc256 = "aesCbc256",
    # XTS-AES 128-bit.
    XtsAes128 = "xtsAes128",
    # XTS-AES 256-bit.
    XtsAes256 = "xtsAes256",

