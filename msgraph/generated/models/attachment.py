from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .entity import Entity
    from .file_attachment import FileAttachment
    from .item_attachment import ItemAttachment
    from .reference_attachment import ReferenceAttachment

from .entity import Entity

@dataclass
class Attachment(Entity, Parsable):
    # The MIME type.
    content_type: Optional[str] = None
    # true if the attachment is an inline attachment; otherwise, false.
    is_inline: Optional[bool] = None
    # The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z
    last_modified_date_time: Optional[datetime.datetime] = None
    # The attachment's file name.
    name: Optional[str] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The length of the attachment in bytes.
    size: Optional[int] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> Attachment:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: Attachment
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        try:
            child_node = parse_node.get_child_node("@odata.type")
            mapping_value = child_node.get_str_value() if child_node else None
        except AttributeError:
            mapping_value = None
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.fileAttachment".casefold():
            from .file_attachment import FileAttachment

            return FileAttachment()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.itemAttachment".casefold():
            from .item_attachment import ItemAttachment

            return ItemAttachment()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.referenceAttachment".casefold():
            from .reference_attachment import ReferenceAttachment

            return ReferenceAttachment()
        return Attachment()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .entity import Entity
        from .file_attachment import FileAttachment
        from .item_attachment import ItemAttachment
        from .reference_attachment import ReferenceAttachment

        from .entity import Entity
        from .file_attachment import FileAttachment
        from .item_attachment import ItemAttachment
        from .reference_attachment import ReferenceAttachment

        fields: dict[str, Callable[[Any], None]] = {
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
        param writer: Serialization writer to use to serialize this model
        Returns: None
        """
        if writer is None:
            raise TypeError("writer cannot be null.")
        super().serialize(writer)
        writer.write_str_value("contentType", self.content_type)
        writer.write_bool_value("isInline", self.is_inline)
        writer.write_datetime_value("lastModifiedDateTime", self.last_modified_date_time)
        writer.write_str_value("name", self.name)
        writer.write_int_value("size", self.size)
    

