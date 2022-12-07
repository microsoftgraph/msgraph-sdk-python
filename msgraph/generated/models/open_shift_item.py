from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

shift_item = lazy_import('msgraph.generated.models.shift_item')

class OpenShiftItem(shift_item.ShiftItem):
    def __init__(self,) -> None:
        """
        Instantiates a new OpenShiftItem and sets the default values.
        """
        super().__init__()
        self.odata_type = "#microsoft.graph.openShiftItem"
        # Count of the number of slots for the given open shift.
        self._open_slot_count: Optional[int] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> OpenShiftItem:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: OpenShiftItem
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return OpenShiftItem()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "open_slot_count": lambda n : setattr(self, 'open_slot_count', n.get_int_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def open_slot_count(self,) -> Optional[int]:
        """
        Gets the openSlotCount property value. Count of the number of slots for the given open shift.
        Returns: Optional[int]
        """
        return self._open_slot_count
    
    @open_slot_count.setter
    def open_slot_count(self,value: Optional[int] = None) -> None:
        """
        Sets the openSlotCount property value. Count of the number of slots for the given open shift.
        Args:
            value: Value to set for the openSlotCount property.
        """
        self._open_slot_count = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_int_value("openSlotCount", self.open_slot_count)
    

