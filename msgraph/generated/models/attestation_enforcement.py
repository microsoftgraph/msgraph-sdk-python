from enum import Enum

class AttestationEnforcement(str, Enum):
    Disabled = "disabled",
    RegistrationOnly = "registrationOnly",
    UnknownFutureValue = "unknownFutureValue",

