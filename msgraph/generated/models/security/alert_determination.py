from enum import Enum

class AlertDetermination(Enum):
    Unknown = "unknown",
    Apt = "apt",
    Malware = "malware",
    SecurityPersonnel = "securityPersonnel",
    SecurityTesting = "securityTesting",
    UnwantedSoftware = "unwantedSoftware",
    Other = "other",
    MultiStagedAttack = "multiStagedAttack",
    CompromisedAccount = "compromisedAccount",
    Phishing = "phishing",
    MaliciousUserActivity = "maliciousUserActivity",
    NotMalicious = "notMalicious",
    NotEnoughDataToValidate = "notEnoughDataToValidate",
    ConfirmedActivity = "confirmedActivity",
    LineOfBusinessApplication = "lineOfBusinessApplication",
    UnknownFutureValue = "unknownFutureValue",

