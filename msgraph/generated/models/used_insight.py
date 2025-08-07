from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .entity import Entity
    from .resource_reference import ResourceReference
    from .resource_visualization import ResourceVisualization
    from .usage_details import UsageDetails

from .entity import Entity

@dataclass
class UsedInsight(Entity, Parsable):
    # Information about when the item was last viewed or modified by the user. Read-only.
    last_used: Optional[UsageDetails] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # Used for navigating to the item that was used. For file attachments, the type is fileAttachment. For linked attachments, the type is driveItem.
    resource: Optional[Entity] = None
    # Reference properties of the used document, such as the URL and type of the document. Read-only
    resource_reference: Optional[ResourceReference] = None
    # Properties that you can use to visualize the document in your experience. Read-only
    resource_visualization: Optional[ResourceVisualization] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> UsedInsight:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: UsedInsight
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return UsedInsight()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .entity import Entity
        from .resource_reference import ResourceReference
        from .resource_visualization import ResourceVisualization
        from .usage_details import UsageDetails

        from .entity import Entity
        from .resource_reference import ResourceReference
        from .resource_visualization import ResourceVisualization
        from .usage_details import UsageDetails

        fields: dict[str, Callable[[Any], None]] = {
            "lastUsed": lambda n : setattr(self, 'last_used', n.get_object_value(UsageDetails)),
            "resource": lambda n : setattr(self, 'resource', n.get_object_value(Entity)),
            "resourceReference": lambda n : setattr(self, 'resource_reference', n.get_object_value(ResourceReference)),
            "resourceVisualization": lambda n : setattr(self, 'resource_visualization', n.get_object_value(ResourceVisualization)),
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
        writer.write_object_value("lastUsed", self.last_used)
        writer.write_object_value("resource", self.resource)
    

