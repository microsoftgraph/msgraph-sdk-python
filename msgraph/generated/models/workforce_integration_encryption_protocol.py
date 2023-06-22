from enum import Enum

class WorkforceIntegrationEncryptionProtocol(str, Enum):
    SharedSecret = "sharedSecret",
    UnknownFutureValue = "unknownFutureValue",

