from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .alert_evidence import AlertEvidence
    from .container_image_evidence import ContainerImageEvidence
    from .kubernetes_pod_evidence import KubernetesPodEvidence

from .alert_evidence import AlertEvidence

@dataclass
class ContainerEvidence(AlertEvidence, Parsable):
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.security.containerEvidence"
    # The list of arguments.
    args: Optional[list[str]] = None
    # The list of commands.
    command: Optional[list[str]] = None
    # The container ID.
    container_id: Optional[str] = None
    # The image used to run the container.
    image: Optional[ContainerImageEvidence] = None
    # The privileged status.
    is_privileged: Optional[bool] = None
    # The container name.
    name: Optional[str] = None
    # The pod this container belongs to.
    pod: Optional[KubernetesPodEvidence] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> ContainerEvidence:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: ContainerEvidence
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return ContainerEvidence()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .alert_evidence import AlertEvidence
        from .container_image_evidence import ContainerImageEvidence
        from .kubernetes_pod_evidence import KubernetesPodEvidence

        from .alert_evidence import AlertEvidence
        from .container_image_evidence import ContainerImageEvidence
        from .kubernetes_pod_evidence import KubernetesPodEvidence

        fields: dict[str, Callable[[Any], None]] = {
            "args": lambda n : setattr(self, 'args', n.get_collection_of_primitive_values(str)),
            "command": lambda n : setattr(self, 'command', n.get_collection_of_primitive_values(str)),
            "containerId": lambda n : setattr(self, 'container_id', n.get_str_value()),
            "image": lambda n : setattr(self, 'image', n.get_object_value(ContainerImageEvidence)),
            "isPrivileged": lambda n : setattr(self, 'is_privileged', n.get_bool_value()),
            "name": lambda n : setattr(self, 'name', n.get_str_value()),
            "pod": lambda n : setattr(self, 'pod', n.get_object_value(KubernetesPodEvidence)),
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
        writer.write_collection_of_primitive_values("args", self.args)
        writer.write_collection_of_primitive_values("command", self.command)
        writer.write_str_value("containerId", self.container_id)
        writer.write_object_value("image", self.image)
        writer.write_bool_value("isPrivileged", self.is_privileged)
        writer.write_str_value("name", self.name)
        writer.write_object_value("pod", self.pod)
    

