from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .alert_evidence import AlertEvidence
    from .kubernetes_platform import KubernetesPlatform

from .alert_evidence import AlertEvidence

@dataclass
class KubernetesClusterEvidence(AlertEvidence):
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.security.kubernetesClusterEvidence"
    # The cloud identifier of the cluster. Can be either an amazonResourceEvidence, azureResourceEvidence, or googleCloudResourceEvidence object.
    cloud_resource: Optional[AlertEvidence] = None
    # The distribution type of the cluster.
    distribution: Optional[str] = None
    # The cluster name.
    name: Optional[str] = None
    # The platform the cluster runs on. Possible values are: unknown, aks, eks, gke, arc, unknownFutureValue.
    platform: Optional[KubernetesPlatform] = None
    # The kubernetes version of the cluster.
    version: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> KubernetesClusterEvidence:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: KubernetesClusterEvidence
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return KubernetesClusterEvidence()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .alert_evidence import AlertEvidence
        from .kubernetes_platform import KubernetesPlatform

        from .alert_evidence import AlertEvidence
        from .kubernetes_platform import KubernetesPlatform

        fields: Dict[str, Callable[[Any], None]] = {
            "cloudResource": lambda n : setattr(self, 'cloud_resource', n.get_object_value(AlertEvidence)),
            "distribution": lambda n : setattr(self, 'distribution', n.get_str_value()),
            "name": lambda n : setattr(self, 'name', n.get_str_value()),
            "platform": lambda n : setattr(self, 'platform', n.get_enum_value(KubernetesPlatform)),
            "version": lambda n : setattr(self, 'version', n.get_str_value()),
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
        writer.write_object_value("cloudResource", self.cloud_resource)
        writer.write_str_value("distribution", self.distribution)
        writer.write_str_value("name", self.name)
        writer.write_enum_value("platform", self.platform)
        writer.write_str_value("version", self.version)
    

