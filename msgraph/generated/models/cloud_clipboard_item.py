from __future__ import annotations
import datetime
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .cloud_clipboard_item_payload import CloudClipboardItemPayload
    from .entity import Entity

from .entity import Entity

@dataclass
class CloudClipboardItem(Entity):
    # Set by the server. DateTime in UTC when the object was created on the server.
    created_date_time: Optional[datetime.datetime] = None
    # Set by the server. DateTime in UTC when the object expires and after that the object is no longer available. The default and also maximum TTL is 12 hours after the creation, but it might change for performance optimization.
    expiration_date_time: Optional[datetime.datetime] = None
    # Set by the server if not provided in the client's request. DateTime in UTC when the object was modified by the client.
    last_modified_date_time: Optional[datetime.datetime] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # A cloudClipboardItem can have multiple cloudClipboardItemPayload objects in the payloads. A window can place more than one clipboard object on the clipboard. Each one represents the same information in a different clipboard format.
    payloads: Optional[List[CloudClipboardItemPayload]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> CloudClipboardItem:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: CloudClipboardItem
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return CloudClipboardItem()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .cloud_clipboard_item_payload import CloudClipboardItemPayload
        from .entity import Entity

        from .cloud_clipboard_item_payload import CloudClipboardItemPayload
        from .entity import Entity

        fields: Dict[str, Callable[[Any], None]] = {
            "createdDateTime": lambda n : setattr(self, 'created_date_time', n.get_datetime_value()),
            "expirationDateTime": lambda n : setattr(self, 'expiration_date_time', n.get_datetime_value()),
            "lastModifiedDateTime": lambda n : setattr(self, 'last_modified_date_time', n.get_datetime_value()),
            "payloads": lambda n : setattr(self, 'payloads', n.get_collection_of_object_values(CloudClipboardItemPayload)),
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
        writer.write_datetime_value("createdDateTime", self.created_date_time)
        writer.write_datetime_value("expirationDateTime", self.expiration_date_time)
        writer.write_datetime_value("lastModifiedDateTime", self.last_modified_date_time)
        writer.write_collection_of_object_values("payloads", self.payloads)
    

