from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .alert_evidence import AlertEvidence
    from .dictionary import Dictionary
    from .ip_evidence import IpEvidence
    from .kubernetes_namespace_evidence import KubernetesNamespaceEvidence
    from .kubernetes_service_port import KubernetesServicePort
    from .kubernetes_service_type import KubernetesServiceType

from .alert_evidence import AlertEvidence

@dataclass
class KubernetesServiceEvidence(AlertEvidence):
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.security.kubernetesServiceEvidence"
    # The service cluster IP.
    cluster_i_p: Optional[IpEvidence] = None
    # The service external IPs.
    external_i_ps: Optional[List[IpEvidence]] = None
    # The service labels.
    labels: Optional[Dictionary] = None
    # The service name.
    name: Optional[str] = None
    # The service namespace.
    namespace: Optional[KubernetesNamespaceEvidence] = None
    # The service selector.
    selector: Optional[Dictionary] = None
    # The list of service ports.
    service_ports: Optional[List[KubernetesServicePort]] = None
    # The serviceType property
    service_type: Optional[KubernetesServiceType] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> KubernetesServiceEvidence:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: KubernetesServiceEvidence
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return KubernetesServiceEvidence()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .alert_evidence import AlertEvidence
        from .dictionary import Dictionary
        from .ip_evidence import IpEvidence
        from .kubernetes_namespace_evidence import KubernetesNamespaceEvidence
        from .kubernetes_service_port import KubernetesServicePort
        from .kubernetes_service_type import KubernetesServiceType

        from .alert_evidence import AlertEvidence
        from .dictionary import Dictionary
        from .ip_evidence import IpEvidence
        from .kubernetes_namespace_evidence import KubernetesNamespaceEvidence
        from .kubernetes_service_port import KubernetesServicePort
        from .kubernetes_service_type import KubernetesServiceType

        fields: Dict[str, Callable[[Any], None]] = {
            "clusterIP": lambda n : setattr(self, 'cluster_i_p', n.get_object_value(IpEvidence)),
            "externalIPs": lambda n : setattr(self, 'external_i_ps', n.get_collection_of_object_values(IpEvidence)),
            "labels": lambda n : setattr(self, 'labels', n.get_object_value(Dictionary)),
            "name": lambda n : setattr(self, 'name', n.get_str_value()),
            "namespace": lambda n : setattr(self, 'namespace', n.get_object_value(KubernetesNamespaceEvidence)),
            "selector": lambda n : setattr(self, 'selector', n.get_object_value(Dictionary)),
            "servicePorts": lambda n : setattr(self, 'service_ports', n.get_collection_of_object_values(KubernetesServicePort)),
            "serviceType": lambda n : setattr(self, 'service_type', n.get_enum_value(KubernetesServiceType)),
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
        writer.write_object_value("clusterIP", self.cluster_i_p)
        writer.write_collection_of_object_values("externalIPs", self.external_i_ps)
        writer.write_object_value("labels", self.labels)
        writer.write_str_value("name", self.name)
        writer.write_object_value("namespace", self.namespace)
        writer.write_object_value("selector", self.selector)
        writer.write_collection_of_object_values("servicePorts", self.service_ports)
        writer.write_enum_value("serviceType", self.service_type)
    

