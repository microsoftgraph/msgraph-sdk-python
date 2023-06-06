from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import entity, resource_reference, resource_visualization, sharing_detail

from . import entity

@dataclass
class SharedInsight(entity.Entity):
    # Details about the shared item. Read only.
    last_shared: Optional[sharing_detail.SharingDetail] = None
    # The lastSharedMethod property
    last_shared_method: Optional[entity.Entity] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # Used for navigating to the item that was shared. For file attachments, the type is fileAttachment. For linked attachments, the type is driveItem.
    resource: Optional[entity.Entity] = None
    # Reference properties of the shared document, such as the url and type of the document. Read-only
    resource_reference: Optional[resource_reference.ResourceReference] = None
    # Properties that you can use to visualize the document in your experience. Read-only
    resource_visualization: Optional[resource_visualization.ResourceVisualization] = None
    # The sharingHistory property
    sharing_history: Optional[List[sharing_detail.SharingDetail]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> SharedInsight:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: SharedInsight
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return SharedInsight()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import entity, resource_reference, resource_visualization, sharing_detail

        fields: Dict[str, Callable[[Any], None]] = {
            "lastShared": lambda n : setattr(self, 'last_shared', n.get_object_value(sharing_detail.SharingDetail)),
            "lastSharedMethod": lambda n : setattr(self, 'last_shared_method', n.get_object_value(entity.Entity)),
            "resource": lambda n : setattr(self, 'resource', n.get_object_value(entity.Entity)),
            "resourceReference": lambda n : setattr(self, 'resource_reference', n.get_object_value(resource_reference.ResourceReference)),
            "resourceVisualization": lambda n : setattr(self, 'resource_visualization', n.get_object_value(resource_visualization.ResourceVisualization)),
            "sharingHistory": lambda n : setattr(self, 'sharing_history', n.get_collection_of_object_values(sharing_detail.SharingDetail)),
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
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_object_value("lastShared", self.last_shared)
        writer.write_object_value("lastSharedMethod", self.last_shared_method)
        writer.write_object_value("resource", self.resource)
        writer.write_collection_of_object_values("sharingHistory", self.sharing_history)
    

