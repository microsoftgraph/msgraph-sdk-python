from enum import Enum

class SslVersion(str, Enum):
    None_ = "none",
    Ssl3_0 = "ssl3_0",
    Tls1_0 = "tls1_0",
    Tls1_1 = "tls1_1",
    Tls1_2 = "tls1_2",
    Tls1_3 = "tls1_3",
    NotSupported = "notSupported",
    UnknownFutureValue = "unknownFutureValue",

