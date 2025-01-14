from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .alert_evidence import AlertEvidence
    from .dictionary import Dictionary
    from .kubernetes_namespace_evidence import KubernetesNamespaceEvidence

from .alert_evidence import AlertEvidence

@dataclass
class KubernetesControllerEvidence(AlertEvidence, Parsable):
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.security.kubernetesControllerEvidence"
    # The labels for the Kubernetes pod.
    labels: Optional[Dictionary] = None
    # The controller name.
    name: Optional[str] = None
    # The service account namespace.
    namespace: Optional[KubernetesNamespaceEvidence] = None
    # The controller type.
    type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> KubernetesControllerEvidence:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: KubernetesControllerEvidence
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return KubernetesControllerEvidence()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .alert_evidence import AlertEvidence
        from .dictionary import Dictionary
        from .kubernetes_namespace_evidence import KubernetesNamespaceEvidence

        from .alert_evidence import AlertEvidence
        from .dictionary import Dictionary
        from .kubernetes_namespace_evidence import KubernetesNamespaceEvidence

        fields: dict[str, Callable[[Any], None]] = {
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
        param writer: Serialization writer to use to serialize this model
        Returns: None
        """
        if writer is None:
            raise TypeError("writer cannot be null.")
        super().serialize(writer)
        writer.write_object_value("labels", self.labels)
        writer.write_str_value("name", self.name)
        writer.write_object_value("namespace", self.namespace)
        writer.write_str_value("type", self.type)
    

