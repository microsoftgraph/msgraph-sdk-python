from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .alert_evidence import AlertEvidence
    from .container_registry_evidence import ContainerRegistryEvidence

from .alert_evidence import AlertEvidence

@dataclass
class ContainerImageEvidence(AlertEvidence, Parsable):
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.security.containerImageEvidence"
    # The digest image entity, in case this is a tag image.
    digest_image: Optional[ContainerImageEvidence] = None
    # The unique identifier for the container image entity.
    image_id: Optional[str] = None
    # The container registry for this image.
    registry: Optional[ContainerRegistryEvidence] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> ContainerImageEvidence:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: ContainerImageEvidence
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return ContainerImageEvidence()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .alert_evidence import AlertEvidence
        from .container_registry_evidence import ContainerRegistryEvidence

        from .alert_evidence import AlertEvidence
        from .container_registry_evidence import ContainerRegistryEvidence

        fields: dict[str, Callable[[Any], None]] = {
            "digestImage": lambda n : setattr(self, 'digest_image', n.get_object_value(ContainerImageEvidence)),
            "imageId": lambda n : setattr(self, 'image_id', n.get_str_value()),
            "registry": lambda n : setattr(self, 'registry', n.get_object_value(ContainerRegistryEvidence)),
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
        writer.write_object_value("digestImage", self.digest_image)
        writer.write_str_value("imageId", self.image_id)
        writer.write_object_value("registry", self.registry)
    

