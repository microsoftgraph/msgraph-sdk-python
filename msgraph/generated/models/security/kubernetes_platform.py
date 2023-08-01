from enum import Enum

class KubernetesPlatform(str, Enum):
    Unknown = "unknown",
    Aks = "aks",
    Eks = "eks",
    Gke = "gke",
    Arc = "arc",
    UnknownFutureValue = "unknownFutureValue",

