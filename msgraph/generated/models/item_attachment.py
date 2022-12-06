from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

attachment = lazy_import('msgraph.generated.models.attachment')
outlook_item = lazy_import('msgraph.generated.models.outlook_item')

class ItemAttachment(attachment.Attachment):
    def __init__(self,) -> None:
        """
        Instantiates a new ItemAttachment and sets the default values.
        """
        super().__init__()
        self.odata_type = "#microsoft.graph.itemAttachment"
        # The attached message or event. Navigation property.
        self._item: Optional[outlook_item.OutlookItem] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> ItemAttachment:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: ItemAttachment
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return ItemAttachment()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "item": lambda n : setattr(self, 'item', n.get_object_value(outlook_item.OutlookItem)),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def item(self,) -> Optional[outlook_item.OutlookItem]:
        """
        Gets the item property value. The attached message or event. Navigation property.
        Returns: Optional[outlook_item.OutlookItem]
        """
        return self._item
    
    @item.setter
    def item(self,value: Optional[outlook_item.OutlookItem] = None) -> None:
        """
        Sets the item property value. The attached message or event. Navigation property.
        Args:
            value: Value to set for the item property.
        """
        self._item = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_object_value("item", self.item)
    

