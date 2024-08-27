from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .alert_evidence import AlertEvidence
    from .container_evidence import ContainerEvidence
    from .dictionary import Dictionary
    from .ip_evidence import IpEvidence
    from .kubernetes_controller_evidence import KubernetesControllerEvidence
    from .kubernetes_namespace_evidence import KubernetesNamespaceEvidence
    from .kubernetes_service_account_evidence import KubernetesServiceAccountEvidence

from .alert_evidence import AlertEvidence

@dataclass
class KubernetesPodEvidence(AlertEvidence):
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.security.kubernetesPodEvidence"
    # The list of pod containers which are not init or ephemeral containers.
    containers: Optional[List[ContainerEvidence]] = None
    # The pod controller.
    controller: Optional[KubernetesControllerEvidence] = None
    # The list of pod ephemeral containers.
    ephemeral_containers: Optional[List[ContainerEvidence]] = None
    # The list of pod init containers.
    init_containers: Optional[List[ContainerEvidence]] = None
    # The pod labels.
    labels: Optional[Dictionary] = None
    # The pod name.
    name: Optional[str] = None
    # The pod namespace.
    namespace: Optional[KubernetesNamespaceEvidence] = None
    # The pod IP.
    pod_ip: Optional[IpEvidence] = None
    # The pod service account.
    service_account: Optional[KubernetesServiceAccountEvidence] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> KubernetesPodEvidence:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: KubernetesPodEvidence
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return KubernetesPodEvidence()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .alert_evidence import AlertEvidence
        from .container_evidence import ContainerEvidence
        from .dictionary import Dictionary
        from .ip_evidence import IpEvidence
        from .kubernetes_controller_evidence import KubernetesControllerEvidence
        from .kubernetes_namespace_evidence import KubernetesNamespaceEvidence
        from .kubernetes_service_account_evidence import KubernetesServiceAccountEvidence

        from .alert_evidence import AlertEvidence
        from .container_evidence import ContainerEvidence
        from .dictionary import Dictionary
        from .ip_evidence import IpEvidence
        from .kubernetes_controller_evidence import KubernetesControllerEvidence
        from .kubernetes_namespace_evidence import KubernetesNamespaceEvidence
        from .kubernetes_service_account_evidence import KubernetesServiceAccountEvidence

        fields: Dict[str, Callable[[Any], None]] = {
            "containers": lambda n : setattr(self, 'containers', n.get_collection_of_object_values(ContainerEvidence)),
            "controller": lambda n : setattr(self, 'controller', n.get_object_value(KubernetesControllerEvidence)),
            "ephemeralContainers": lambda n : setattr(self, 'ephemeral_containers', n.get_collection_of_object_values(ContainerEvidence)),
            "initContainers": lambda n : setattr(self, 'init_containers', n.get_collection_of_object_values(ContainerEvidence)),
            "labels": lambda n : setattr(self, 'labels', n.get_object_value(Dictionary)),
            "name": lambda n : setattr(self, 'name', n.get_str_value()),
            "namespace": lambda n : setattr(self, 'namespace', n.get_object_value(KubernetesNamespaceEvidence)),
            "podIp": lambda n : setattr(self, 'pod_ip', n.get_object_value(IpEvidence)),
            "serviceAccount": lambda n : setattr(self, 'service_account', n.get_object_value(KubernetesServiceAccountEvidence)),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        param writer: Serialization writer to use to serialize this model
        Returns: None
        """
        if writer is None:
            raise TypeError("writer cannot be null.")
        super().serialize(writer)
        writer.write_collection_of_object_values("containers", self.containers)
        writer.write_object_value("controller", self.controller)
        writer.write_collection_of_object_values("ephemeralContainers", self.ephemeral_containers)
        writer.write_collection_of_object_values("initContainers", self.init_containers)
        writer.write_object_value("labels", self.labels)
        writer.write_str_value("name", self.name)
        writer.write_object_value("namespace", self.namespace)
        writer.write_object_value("podIp", self.pod_ip)
        writer.write_object_value("serviceAccount", self.service_account)
    

