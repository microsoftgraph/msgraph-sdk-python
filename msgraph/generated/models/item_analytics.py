from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

entity = lazy_import('msgraph.generated.models.entity')
item_activity_stat = lazy_import('msgraph.generated.models.item_activity_stat')

class ItemAnalytics(entity.Entity):
    @property
    def all_time(self,) -> Optional[item_activity_stat.ItemActivityStat]:
        """
        Gets the allTime property value. The allTime property
        Returns: Optional[item_activity_stat.ItemActivityStat]
        """
        return self._all_time
    
    @all_time.setter
    def all_time(self,value: Optional[item_activity_stat.ItemActivityStat] = None) -> None:
        """
        Sets the allTime property value. The allTime property
        Args:
            value: Value to set for the allTime property.
        """
        self._all_time = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new itemAnalytics and sets the default values.
        """
        super().__init__()
        # The allTime property
        self._all_time: Optional[item_activity_stat.ItemActivityStat] = None
        # The itemActivityStats property
        self._item_activity_stats: Optional[List[item_activity_stat.ItemActivityStat]] = None
        # The lastSevenDays property
        self._last_seven_days: Optional[item_activity_stat.ItemActivityStat] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
    
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
        fields = {
            "all_time": lambda n : setattr(self, 'all_time', n.get_object_value(item_activity_stat.ItemActivityStat)),
            "item_activity_stats": lambda n : setattr(self, 'item_activity_stats', n.get_collection_of_object_values(item_activity_stat.ItemActivityStat)),
            "last_seven_days": lambda n : setattr(self, 'last_seven_days', n.get_object_value(item_activity_stat.ItemActivityStat)),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def item_activity_stats(self,) -> Optional[List[item_activity_stat.ItemActivityStat]]:
        """
        Gets the itemActivityStats property value. The itemActivityStats property
        Returns: Optional[List[item_activity_stat.ItemActivityStat]]
        """
        return self._item_activity_stats
    
    @item_activity_stats.setter
    def item_activity_stats(self,value: Optional[List[item_activity_stat.ItemActivityStat]] = None) -> None:
        """
        Sets the itemActivityStats property value. The itemActivityStats property
        Args:
            value: Value to set for the itemActivityStats property.
        """
        self._item_activity_stats = value
    
    @property
    def last_seven_days(self,) -> Optional[item_activity_stat.ItemActivityStat]:
        """
        Gets the lastSevenDays property value. The lastSevenDays property
        Returns: Optional[item_activity_stat.ItemActivityStat]
        """
        return self._last_seven_days
    
    @last_seven_days.setter
    def last_seven_days(self,value: Optional[item_activity_stat.ItemActivityStat] = None) -> None:
        """
        Sets the lastSevenDays property value. The lastSevenDays property
        Args:
            value: Value to set for the lastSevenDays property.
        """
        self._last_seven_days = value
    
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
    

