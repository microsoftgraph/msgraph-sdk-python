from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .alert_evidence import AlertEvidence
    from .dictionary import Dictionary
    from .kubernetes_cluster_evidence import KubernetesClusterEvidence

from .alert_evidence import AlertEvidence

@dataclass
class KubernetesNamespaceEvidence(AlertEvidence):
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.security.kubernetesNamespaceEvidence"
    # The namespace cluster.
    cluster: Optional[KubernetesClusterEvidence] = None
    # The labels for the Kubernetes pod.
    labels: Optional[Dictionary] = None
    # The namespace name.
    name: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> KubernetesNamespaceEvidence:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: KubernetesNamespaceEvidence
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return KubernetesNamespaceEvidence()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .alert_evidence import AlertEvidence
        from .dictionary import Dictionary
        from .kubernetes_cluster_evidence import KubernetesClusterEvidence

        from .alert_evidence import AlertEvidence
        from .dictionary import Dictionary
        from .kubernetes_cluster_evidence import KubernetesClusterEvidence

        fields: Dict[str, Callable[[Any], None]] = {
            "cluster": lambda n : setattr(self, 'cluster', n.get_object_value(KubernetesClusterEvidence)),
            "labels": lambda n : setattr(self, 'labels', n.get_object_value(Dictionary)),
            "name": lambda n : setattr(self, 'name', n.get_str_value()),
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
        writer.write_object_value("cluster", self.cluster)
        writer.write_object_value("labels", self.labels)
        writer.write_str_value("name", self.name)
    

