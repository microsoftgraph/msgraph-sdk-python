from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .entity import Entity
    from .service_health import ServiceHealth
    from .service_health_issue import ServiceHealthIssue
    from .service_update_message import ServiceUpdateMessage

from .entity import Entity

@dataclass
class ServiceAnnouncement(Entity, Parsable):
    # A collection of service health information for tenant. This property is a contained navigation property, it is nullable and readonly.
    health_overviews: Optional[list[ServiceHealth]] = None
    # A collection of service issues for tenant. This property is a contained navigation property, it is nullable and readonly.
    issues: Optional[list[ServiceHealthIssue]] = None
    # A collection of service messages for tenant. This property is a contained navigation property, it is nullable and readonly.
    messages: Optional[list[ServiceUpdateMessage]] = None
    # The OdataType property
    odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> ServiceAnnouncement:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: ServiceAnnouncement
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return ServiceAnnouncement()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .entity import Entity
        from .service_health import ServiceHealth
        from .service_health_issue import ServiceHealthIssue
        from .service_update_message import ServiceUpdateMessage

        from .entity import Entity
        from .service_health import ServiceHealth
        from .service_health_issue import ServiceHealthIssue
        from .service_update_message import ServiceUpdateMessage

        fields: dict[str, Callable[[Any], None]] = {
            "healthOverviews": lambda n : setattr(self, 'health_overviews', n.get_collection_of_object_values(ServiceHealth)),
            "issues": lambda n : setattr(self, 'issues', n.get_collection_of_object_values(ServiceHealthIssue)),
            "messages": lambda n : setattr(self, 'messages', n.get_collection_of_object_values(ServiceUpdateMessage)),
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
        writer.write_collection_of_object_values("healthOverviews", self.health_overviews)
        writer.write_collection_of_object_values("issues", self.issues)
        writer.write_collection_of_object_values("messages", self.messages)
    

