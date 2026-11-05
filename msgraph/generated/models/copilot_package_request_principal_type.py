from enum import Enum

class CopilotPackageRequestPrincipalType(str, Enum):
    # An explicit user principal.
    User = "user",
    # An explicit group principal; group membership is not expanded.
    Group = "group",
    # An agent application identifier reported by Governance. Not assumed to be a service principal object identifier.
    AgentApplication = "agentApplication",
    # An agent user principal.
    AgentUser = "agentUser",
    # An evolvable value also used when the source principal kind is missing or unrecognized.
    UnknownFutureValue = "unknownFutureValue",

