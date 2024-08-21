from __future__ import annotations
import datetime
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .entity import Entity
    from .incomplete_data import IncompleteData
    from .item_action_stat import ItemActionStat
    from .item_activity import ItemActivity

from .entity import Entity

@dataclass
class ItemActivityStat(Entity):
    # Statistics about the access actions in this interval. Read-only.
    access: Optional[ItemActionStat] = None
    # Exposes the itemActivities represented in this itemActivityStat resource.
    activities: Optional[List[ItemActivity]] = None
    # Statistics about the create actions in this interval. Read-only.
    create: Optional[ItemActionStat] = None
    # Statistics about the delete actions in this interval. Read-only.
    delete: Optional[ItemActionStat] = None
    # Statistics about the edit actions in this interval. Read-only.
    edit: Optional[ItemActionStat] = None
    # When the interval ends. Read-only.
    end_date_time: Optional[datetime.datetime] = None
    # Indicates that the statistics in this interval are based on incomplete data. Read-only.
    incomplete_data: Optional[IncompleteData] = None
    # Indicates whether the item is 'trending.' Read-only.
    is_trending: Optional[bool] = None
    # Statistics about the move actions in this interval. Read-only.
    move: Optional[ItemActionStat] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # When the interval starts. Read-only.
    start_date_time: Optional[datetime.datetime] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> ItemActivityStat:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: ItemActivityStat
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return ItemActivityStat()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .entity import Entity
        from .incomplete_data import IncompleteData
        from .item_action_stat import ItemActionStat
        from .item_activity import ItemActivity

        from .entity import Entity
        from .incomplete_data import IncompleteData
        from .item_action_stat import ItemActionStat
        from .item_activity import ItemActivity

        fields: Dict[str, Callable[[Any], None]] = {
            "access": lambda n : setattr(self, 'access', n.get_object_value(ItemActionStat)),
            "activities": lambda n : setattr(self, 'activities', n.get_collection_of_object_values(ItemActivity)),
            "create": lambda n : setattr(self, 'create', n.get_object_value(ItemActionStat)),
            "delete": lambda n : setattr(self, 'delete', n.get_object_value(ItemActionStat)),
            "edit": lambda n : setattr(self, 'edit', n.get_object_value(ItemActionStat)),
            "endDateTime": lambda n : setattr(self, 'end_date_time', n.get_datetime_value()),
            "incompleteData": lambda n : setattr(self, 'incomplete_data', n.get_object_value(IncompleteData)),
            "isTrending": lambda n : setattr(self, 'is_trending', n.get_bool_value()),
            "move": lambda n : setattr(self, 'move', n.get_object_value(ItemActionStat)),
            "startDateTime": lambda n : setattr(self, 'start_date_time', n.get_datetime_value()),
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
        writer.write_object_value("access", self.access)
        writer.write_collection_of_object_values("activities", self.activities)
        writer.write_object_value("create", self.create)
        writer.write_object_value("delete", self.delete)
        writer.write_object_value("edit", self.edit)
        writer.write_datetime_value("endDateTime", self.end_date_time)
        writer.write_object_value("incompleteData", self.incomplete_data)
        writer.write_bool_value("isTrending", self.is_trending)
        writer.write_object_value("move", self.move)
        writer.write_datetime_value("startDateTime", self.start_date_time)
    

