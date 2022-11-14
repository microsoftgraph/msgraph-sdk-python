from enum import Enum

class FederatedIdpMfaBehavior(Enum):
    AcceptIfMfaDoneByFederatedIdp = "acceptIfMfaDoneByFederatedIdp",
    EnforceMfaByFederatedIdp = "enforceMfaByFederatedIdp",
    RejectMfaByFederatedIdp = "rejectMfaByFederatedIdp",
    UnknownFutureValue = "unknownFutureValue",

