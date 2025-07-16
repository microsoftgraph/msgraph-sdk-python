from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .entity import Entity
    from .item_activity_stat import ItemActivityStat

from .entity import Entity

@dataclass
class ItemAnalytics(Entity, Parsable):
    # The allTime property
    all_time: Optional[ItemActivityStat] = None
    # The itemActivityStats property
    item_activity_stats: Optional[list[ItemActivityStat]] = None
    # The lastSevenDays property
    last_seven_days: Optional[ItemActivityStat] = None
    # The OdataType property
    odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> ItemAnalytics:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: ItemAnalytics
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return ItemAnalytics()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .entity import Entity
        from .item_activity_stat import ItemActivityStat

        from .entity import Entity
        from .item_activity_stat import ItemActivityStat

        fields: dict[str, Callable[[Any], None]] = {
            "allTime": lambda n : setattr(self, 'all_time', n.get_object_value(ItemActivityStat)),
            "itemActivityStats": lambda n : setattr(self, 'item_activity_stats', n.get_collection_of_object_values(ItemActivityStat)),
            "lastSevenDays": lambda n : setattr(self, 'last_seven_days', n.get_object_value(ItemActivityStat)),
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
        writer.write_object_value("allTime", self.all_time)
        writer.write_collection_of_object_values("itemActivityStats", self.item_activity_stats)
        writer.write_object_value("lastSevenDays", self.last_seven_days)
    

