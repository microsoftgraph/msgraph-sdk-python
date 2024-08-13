from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .alert_evidence import AlertEvidence
    from .kubernetes_namespace_evidence import KubernetesNamespaceEvidence

from .alert_evidence import AlertEvidence

@dataclass
class KubernetesSecretEvidence(AlertEvidence):
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.security.kubernetesSecretEvidence"
    # The secret name.
    name: Optional[str] = None
    # The secret namespace.
    namespace: Optional[KubernetesNamespaceEvidence] = None
    # The secret type can include both built-in types and custom ones. Examples of built-in types are: Opaque, kubernetes.io/service-account-token, kubernetes.io/dockercfg, kubernetes.io/dockerconfigjson, kubernetes.io/basic-auth, kubernetes.io/ssh-auth, kubernetes.io/tls, bootstrap.kubernetes.io/token.
    secret_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> KubernetesSecretEvidence:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: KubernetesSecretEvidence
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return KubernetesSecretEvidence()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .alert_evidence import AlertEvidence
        from .kubernetes_namespace_evidence import KubernetesNamespaceEvidence

        from .alert_evidence import AlertEvidence
        from .kubernetes_namespace_evidence import KubernetesNamespaceEvidence

        fields: Dict[str, Callable[[Any], None]] = {
            "name": lambda n : setattr(self, 'name', n.get_str_value()),
            "namespace": lambda n : setattr(self, 'namespace', n.get_object_value(KubernetesNamespaceEvidence)),
            "secretType": lambda n : setattr(self, 'secret_type', n.get_str_value()),
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
        writer.write_str_value("name", self.name)
        writer.write_object_value("namespace", self.namespace)
        writer.write_str_value("secretType", self.secret_type)
    

