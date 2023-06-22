from __future__ import annotations
from dataclasses import dataclass, field
from datetime import datetime
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import entity, file_attachment, item_attachment, reference_attachment

from . import entity

@dataclass
class Attachment(entity.Entity):
    # The MIME type.
    content_type: Optional[str] = None
    # true if the attachment is an inline attachment; otherwise, false.
    is_inline: Optional[bool] = None
    # The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z
    last_modified_date_time: Optional[datetime] = None
    # The attachment's file name.
    name: Optional[str] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The length of the attachment in bytes.
    size: Optional[int] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> Attachment:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: Attachment
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        try:
            mapping_value = parse_node.get_child_node("@odata.type").get_str_value()
        except AttributeError:
            mapping_value = None
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.fileAttachment".casefold():
            from . import file_attachment

            return file_attachment.FileAttachment()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.itemAttachment".casefold():
            from . import item_attachment

            return item_attachment.ItemAttachment()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.referenceAttachment".casefold():
            from . import reference_attachment

            return reference_attachment.ReferenceAttachment()
        return Attachment()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import entity, file_attachment, item_attachment, reference_attachment

        from . import entity, file_attachment, item_attachment, reference_attachment

        fields: Dict[str, Callable[[Any], None]] = {
            "contentType": lambda n : setattr(self, 'content_type', n.get_str_value()),
            "isInline": lambda n : setattr(self, 'is_inline', n.get_bool_value()),
            "lastModifiedDateTime": lambda n : setattr(self, 'last_modified_date_time', n.get_datetime_value()),
            "name": lambda n : setattr(self, 'name', n.get_str_value()),
            "size": lambda n : setattr(self, 'size', n.get_int_value()),
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
        if not writer:
            raise TypeError("writer cannot be null.")
        super().serialize(writer)
        writer.write_str_value("contentType", self.content_type)
        writer.write_bool_value("isInline", self.is_inline)
        writer.write_datetime_value("lastModifiedDateTime", self.last_modified_date_time)
        writer.write_str_value("name", self.name)
        writer.write_int_value("size", self.size)
    

