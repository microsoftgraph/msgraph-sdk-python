from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import entity, item_activity_stat

from . import entity

@dataclass
class ItemAnalytics(entity.Entity):
    # The allTime property
    all_time: Optional[item_activity_stat.ItemActivityStat] = None
    # The itemActivityStats property
    item_activity_stats: Optional[List[item_activity_stat.ItemActivityStat]] = None
    # The lastSevenDays property
    last_seven_days: Optional[item_activity_stat.ItemActivityStat] = None
    # The OdataType property
    odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> ItemAnalytics:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: ItemAnalytics
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return ItemAnalytics()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import entity, item_activity_stat

        fields: Dict[str, Callable[[Any], None]] = {
            "allTime": lambda n : setattr(self, 'all_time', n.get_object_value(item_activity_stat.ItemActivityStat)),
            "itemActivityStats": lambda n : setattr(self, 'item_activity_stats', n.get_collection_of_object_values(item_activity_stat.ItemActivityStat)),
            "lastSevenDays": lambda n : setattr(self, 'last_seven_days', n.get_object_value(item_activity_stat.ItemActivityStat)),
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
        writer.write_object_value("allTime", self.all_time)
        writer.write_collection_of_object_values("itemActivityStats", self.item_activity_stats)
        writer.write_object_value("lastSevenDays", self.last_seven_days)
    

