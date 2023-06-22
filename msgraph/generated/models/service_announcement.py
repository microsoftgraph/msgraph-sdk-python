from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import entity, service_health, service_health_issue, service_update_message

from . import entity

@dataclass
class ServiceAnnouncement(entity.Entity):
    # A collection of service health information for tenant. This property is a contained navigation property, it is nullable and readonly.
    health_overviews: Optional[List[service_health.ServiceHealth]] = None
    # A collection of service issues for tenant. This property is a contained navigation property, it is nullable and readonly.
    issues: Optional[List[service_health_issue.ServiceHealthIssue]] = None
    # A collection of service messages for tenant. This property is a contained navigation property, it is nullable and readonly.
    messages: Optional[List[service_update_message.ServiceUpdateMessage]] = None
    # The OdataType property
    odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> ServiceAnnouncement:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: ServiceAnnouncement
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return ServiceAnnouncement()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import entity, service_health, service_health_issue, service_update_message

        from . import entity, service_health, service_health_issue, service_update_message

        fields: Dict[str, Callable[[Any], None]] = {
            "healthOverviews": lambda n : setattr(self, 'health_overviews', n.get_collection_of_object_values(service_health.ServiceHealth)),
            "issues": lambda n : setattr(self, 'issues', n.get_collection_of_object_values(service_health_issue.ServiceHealthIssue)),
            "messages": lambda n : setattr(self, 'messages', n.get_collection_of_object_values(service_update_message.ServiceUpdateMessage)),
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
        writer.write_collection_of_object_values("healthOverviews", self.health_overviews)
        writer.write_collection_of_object_values("issues", self.issues)
        writer.write_collection_of_object_values("messages", self.messages)
    

