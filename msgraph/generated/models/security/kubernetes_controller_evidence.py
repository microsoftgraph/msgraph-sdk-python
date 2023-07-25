from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .alert_evidence import AlertEvidence
    from .dictionary import Dictionary
    from .kubernetes_namespace_evidence import KubernetesNamespaceEvidence

from .alert_evidence import AlertEvidence

@dataclass
class KubernetesControllerEvidence(AlertEvidence):
    odata_type = "#microsoft.graph.security.kubernetesControllerEvidence"
    # The labels property
    labels: Optional[Dictionary] = None
    # The name property
    name: Optional[str] = None
    # The namespace property
    namespace: Optional[KubernetesNamespaceEvidence] = None
    # The type property
    type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> KubernetesControllerEvidence:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parse_node: The parse node to use to read the discriminator value and create the object
        Returns: KubernetesControllerEvidence
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return KubernetesControllerEvidence()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .alert_evidence import AlertEvidence
        from .dictionary import Dictionary
        from .kubernetes_namespace_evidence import KubernetesNamespaceEvidence

        from .alert_evidence import AlertEvidence
        from .dictionary import Dictionary
        from .kubernetes_namespace_evidence import KubernetesNamespaceEvidence

        fields: Dict[str, Callable[[Any], None]] = {
            "labels": lambda n : setattr(self, 'labels', n.get_object_value(Dictionary)),
            "name": lambda n : setattr(self, 'name', n.get_str_value()),
            "namespace": lambda n : setattr(self, 'namespace', n.get_object_value(KubernetesNamespaceEvidence)),
            "type": lambda n : setattr(self, 'type', n.get_str_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if not writer:
            raise TypeError("writer cannot be null.")
        super().serialize(writer)
        writer.write_object_value("labels", self.labels)
        writer.write_str_value("name", self.name)
        writer.write_object_value("namespace", self.namespace)
        writer.write_str_value("type", self.type)
    

