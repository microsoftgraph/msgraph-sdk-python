from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .change_tracked_entity import ChangeTrackedEntity

from .change_tracked_entity import ChangeTrackedEntity

@dataclass
class SchedulingGroup(ChangeTrackedEntity, Parsable):
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.schedulingGroup"
    # The display name for the schedulingGroup. Required.
    display_name: Optional[str] = None
    # Indicates whether the schedulingGroup can be used when creating new entities or updating existing ones. Required.
    is_active: Optional[bool] = None
    # The list of user IDs that are a member of the schedulingGroup. Required.
    user_ids: Optional[List[str]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> SchedulingGroup:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: SchedulingGroup
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return SchedulingGroup()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .change_tracked_entity import ChangeTrackedEntity

        from .change_tracked_entity import ChangeTrackedEntity

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
        param writer: Serialization writer to use to serialize this model
        Returns: None
        """
        if writer is None:
            raise TypeError("writer cannot be null.")
        super().serialize(writer)
        from .change_tracked_entity import ChangeTrackedEntity

        writer.write_str_value("displayName", self.display_name)
        writer.write_collection_of_primitive_values("userIds", self.user_ids)
    

