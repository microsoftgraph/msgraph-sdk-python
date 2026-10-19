from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .attachment import Attachment
    from .extension import Extension
    from .item_body import ItemBody
    from .multi_value_legacy_extended_property import MultiValueLegacyExtendedProperty
    from .outlook_item import OutlookItem
    from .single_value_legacy_extended_property import SingleValueLegacyExtendedProperty

from .outlook_item import OutlookItem

@dataclass
class Note(OutlookItem, Parsable):
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.note"
    # The file attachments for the note. Only inline image attachments (image/png, image/jpeg, image/gif, or image/bmp) are supported, with a maximum size of 3 MB per attachment. Use $expand to retrieve attachments.
    attachments: Optional[list[Attachment]] = None
    # The content of the note. Supports text or html content types.
    body: Optional[ItemBody] = None
    # Auto-generated preview of the note body content (first ~255 characters, plain text). Read-only.
    body_preview: Optional[str] = None
    # The collection of open extensions defined for the note.
    extensions: Optional[list[Extension]] = None
    # Indicates whether the note has file attachments. Supports $filter (eq). Read-only.
    has_attachments: Optional[bool] = None
    # Indicates whether the note is soft-deleted. Read-only.
    is_deleted: Optional[bool] = None
    # The collection of multi-value extended properties defined for the note.
    multi_value_extended_properties: Optional[list[MultiValueLegacyExtendedProperty]] = None
    # The collection of single-value extended properties defined for the note.
    single_value_extended_properties: Optional[list[SingleValueLegacyExtendedProperty]] = None
    # The title of the note. Supports $filter (eq, ne, startsWith) and $orderby.
    subject: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> Note:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: Note
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return Note()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .attachment import Attachment
        from .extension import Extension
        from .item_body import ItemBody
        from .multi_value_legacy_extended_property import MultiValueLegacyExtendedProperty
        from .outlook_item import OutlookItem
        from .single_value_legacy_extended_property import SingleValueLegacyExtendedProperty

        from .attachment import Attachment
        from .extension import Extension
        from .item_body import ItemBody
        from .multi_value_legacy_extended_property import MultiValueLegacyExtendedProperty
        from .outlook_item import OutlookItem
        from .single_value_legacy_extended_property import SingleValueLegacyExtendedProperty

        fields: dict[str, Callable[[Any], None]] = {
            "attachments": lambda n : setattr(self, 'attachments', n.get_collection_of_object_values(Attachment)),
            "body": lambda n : setattr(self, 'body', n.get_object_value(ItemBody)),
            "bodyPreview": lambda n : setattr(self, 'body_preview', n.get_str_value()),
            "extensions": lambda n : setattr(self, 'extensions', n.get_collection_of_object_values(Extension)),
            "hasAttachments": lambda n : setattr(self, 'has_attachments', n.get_bool_value()),
            "isDeleted": lambda n : setattr(self, 'is_deleted', n.get_bool_value()),
            "multiValueExtendedProperties": lambda n : setattr(self, 'multi_value_extended_properties', n.get_collection_of_object_values(MultiValueLegacyExtendedProperty)),
            "singleValueExtendedProperties": lambda n : setattr(self, 'single_value_extended_properties', n.get_collection_of_object_values(SingleValueLegacyExtendedProperty)),
            "subject": lambda n : setattr(self, 'subject', n.get_str_value()),
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
        writer.write_collection_of_object_values("attachments", self.attachments)
        writer.write_object_value("body", self.body)
        writer.write_collection_of_object_values("extensions", self.extensions)
        writer.write_collection_of_object_values("multiValueExtendedProperties", self.multi_value_extended_properties)
        writer.write_collection_of_object_values("singleValueExtendedProperties", self.single_value_extended_properties)
        writer.write_str_value("subject", self.subject)
    

