from enum import Enum

class TemplateScenarios(str, Enum):
    New = "new",
    SecureFoundation = "secureFoundation",
    ZeroTrust = "zeroTrust",
    RemoteWork = "remoteWork",
    ProtectAdmins = "protectAdmins",
    EmergingThreats = "emergingThreats",
    UnknownFutureValue = "unknownFutureValue",

