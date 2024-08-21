from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .entity import Entity
    from .resource_reference import ResourceReference
    from .resource_visualization import ResourceVisualization
    from .sharing_detail import SharingDetail

from .entity import Entity

@dataclass
class SharedInsight(Entity):
    # Details about the shared item. Read only.
    last_shared: Optional[SharingDetail] = None
    # The lastSharedMethod property
    last_shared_method: Optional[Entity] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # Used for navigating to the item that was shared. For file attachments, the type is fileAttachment. For linked attachments, the type is driveItem.
    resource: Optional[Entity] = None
    # Reference properties of the shared document, such as the url and type of the document. Read-only
    resource_reference: Optional[ResourceReference] = None
    # Properties that you can use to visualize the document in your experience. Read-only
    resource_visualization: Optional[ResourceVisualization] = None
    # The sharingHistory property
    sharing_history: Optional[List[SharingDetail]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> SharedInsight:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: SharedInsight
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return SharedInsight()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .entity import Entity
        from .resource_reference import ResourceReference
        from .resource_visualization import ResourceVisualization
        from .sharing_detail import SharingDetail

        from .entity import Entity
        from .resource_reference import ResourceReference
        from .resource_visualization import ResourceVisualization
        from .sharing_detail import SharingDetail

        fields: Dict[str, Callable[[Any], None]] = {
            "lastShared": lambda n : setattr(self, 'last_shared', n.get_object_value(SharingDetail)),
            "lastSharedMethod": lambda n : setattr(self, 'last_shared_method', n.get_object_value(Entity)),
            "resource": lambda n : setattr(self, 'resource', n.get_object_value(Entity)),
            "resourceReference": lambda n : setattr(self, 'resource_reference', n.get_object_value(ResourceReference)),
            "resourceVisualization": lambda n : setattr(self, 'resource_visualization', n.get_object_value(ResourceVisualization)),
            "sharingHistory": lambda n : setattr(self, 'sharing_history', n.get_collection_of_object_values(SharingDetail)),
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
        writer.write_object_value("lastShared", self.last_shared)
        writer.write_object_value("lastSharedMethod", self.last_shared_method)
        writer.write_object_value("resource", self.resource)
        writer.write_collection_of_object_values("sharingHistory", self.sharing_history)
    

