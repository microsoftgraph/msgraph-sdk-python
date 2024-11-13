from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .shift_item import ShiftItem

from .shift_item import ShiftItem

@dataclass
class OpenShiftItem(ShiftItem, Parsable):
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.openShiftItem"
    # Count of the number of slots for the given open shift.
    open_slot_count: Optional[int] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> OpenShiftItem:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: OpenShiftItem
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return OpenShiftItem()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .shift_item import ShiftItem

        from .shift_item import ShiftItem

        fields: Dict[str, Callable[[Any], None]] = {
            "openSlotCount": lambda n : setattr(self, 'open_slot_count', n.get_int_value()),
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
        from .shift_item import ShiftItem

        writer.write_int_value("openSlotCount", self.open_slot_count)
    

