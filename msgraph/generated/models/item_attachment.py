from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .attachment import Attachment
    from .outlook_item import OutlookItem

from .attachment import Attachment

@dataclass
class ItemAttachment(Attachment, Parsable):
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.itemAttachment"
    # The attached message or event. Navigation property.
    item: Optional[OutlookItem] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> ItemAttachment:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: ItemAttachment
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return ItemAttachment()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .attachment import Attachment
        from .outlook_item import OutlookItem

        from .attachment import Attachment
        from .outlook_item import OutlookItem

        fields: Dict[str, Callable[[Any], None]] = {
            "item": lambda n : setattr(self, 'item', n.get_object_value(OutlookItem)),
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
        from .attachment import Attachment
        from .outlook_item import OutlookItem

        writer.write_object_value("item", self.item)
    

