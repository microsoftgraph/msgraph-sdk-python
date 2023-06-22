from enum import Enum

class ConnectedOrganizationState(str, Enum):
    Configured = "configured",
    Proposed = "proposed",
    UnknownFutureValue = "unknownFutureValue",

