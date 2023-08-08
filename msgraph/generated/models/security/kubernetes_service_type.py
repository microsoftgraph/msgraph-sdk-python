from enum import Enum

class KubernetesServiceType(str, Enum):
    Unknown = "unknown",
    ClusterIP = "clusterIP",
    ExternalName = "externalName",
    NodePort = "nodePort",
    LoadBalancer = "loadBalancer",
    UnknownFutureValue = "unknownFutureValue",

