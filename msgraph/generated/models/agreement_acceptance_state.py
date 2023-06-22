from enum import Enum

class AgreementAcceptanceState(str, Enum):
    Accepted = "accepted",
    Declined = "declined",
    UnknownFutureValue = "unknownFutureValue",

