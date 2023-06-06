from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import change_tracked_entity

from . import change_tracked_entity

@dataclass
class SchedulingGroup(change_tracked_entity.ChangeTrackedEntity):
    odata_type = "#microsoft.graph.schedulingGroup"
    # The display name for the schedulingGroup. Required.
    display_name: Optional[str] = None
    # Indicates whether the schedulingGroup can be used when creating new entities or updating existing ones. Required.
    is_active: Optional[bool] = None
    # The list of user IDs that are a member of the schedulingGroup. Required.
    user_ids: Optional[List[str]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> SchedulingGroup:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: SchedulingGroup
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return SchedulingGroup()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import change_tracked_entity

        fields: Dict[str, Callable[[Any], None]] = {
            "displayName": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "isActive": lambda n : setattr(self, 'is_active', n.get_bool_value()),
            "userIds": lambda n : setattr(self, 'user_ids', n.get_collection_of_primitive_values(str)),
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
        writer.write_str_value("displayName", self.display_name)
        writer.write_collection_of_primitive_values("userIds", self.user_ids)
    

