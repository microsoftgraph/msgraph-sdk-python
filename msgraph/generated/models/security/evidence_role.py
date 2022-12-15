from enum import Enum

class EvidenceRole(Enum):
    Unknown = "unknown",
    Contextual = "contextual",
    Scanned = "scanned",
    Source = "source",
    Destination = "destination",
    Created = "created",
    Added = "added",
    Compromised = "compromised",
    Edited = "edited",
    Attacked = "attacked",
    Attacker = "attacker",
    CommandAndControl = "commandAndControl",
    Loaded = "loaded",
    Suspicious = "suspicious",
    PolicyViolator = "policyViolator",
    UnknownFutureValue = "unknownFutureValue",

