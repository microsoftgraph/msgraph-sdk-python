from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .base_item import BaseItem
    from .content_type_info import ContentTypeInfo
    from .deleted import Deleted
    from .document_set_version import DocumentSetVersion
    from .drive_item import DriveItem
    from .field_value_set import FieldValueSet
    from .item_analytics import ItemAnalytics
    from .list_item_version import ListItemVersion
    from .sharepoint_ids import SharepointIds

from .base_item import BaseItem

@dataclass
class ListItem(BaseItem, Parsable):
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.listItem"
    # Analytics about the view activities that took place on this item.
    analytics: Optional[ItemAnalytics] = None
    # The content type of this list item
    content_type: Optional[ContentTypeInfo] = None
    # If present in the result of a delta enumeration, indicates that the item was deleted. Read-only.
    deleted: Optional[Deleted] = None
    # Version information for a document set version created by a user.
    document_set_versions: Optional[list[DocumentSetVersion]] = None
    # For document libraries, the driveItem relationship exposes the listItem as a driveItem
    drive_item: Optional[DriveItem] = None
    # The values of the columns set on this list item.
    fields: Optional[FieldValueSet] = None
    # Returns identifiers useful for SharePoint REST compatibility. Read-only.
    sharepoint_ids: Optional[SharepointIds] = None
    # The list of previous versions of the list item.
    versions: Optional[list[ListItemVersion]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> ListItem:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: ListItem
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return ListItem()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .base_item import BaseItem
        from .content_type_info import ContentTypeInfo
        from .deleted import Deleted
        from .document_set_version import DocumentSetVersion
        from .drive_item import DriveItem
        from .field_value_set import FieldValueSet
        from .item_analytics import ItemAnalytics
        from .list_item_version import ListItemVersion
        from .sharepoint_ids import SharepointIds

        from .base_item import BaseItem
        from .content_type_info import ContentTypeInfo
        from .deleted import Deleted
        from .document_set_version import DocumentSetVersion
        from .drive_item import DriveItem
        from .field_value_set import FieldValueSet
        from .item_analytics import ItemAnalytics
        from .list_item_version import ListItemVersion
        from .sharepoint_ids import SharepointIds

        fields: dict[str, Callable[[Any], None]] = {
            "analytics": lambda n : setattr(self, 'analytics', n.get_object_value(ItemAnalytics)),
            "contentType": lambda n : setattr(self, 'content_type', n.get_object_value(ContentTypeInfo)),
            "deleted": lambda n : setattr(self, 'deleted', n.get_object_value(Deleted)),
            "documentSetVersions": lambda n : setattr(self, 'document_set_versions', n.get_collection_of_object_values(DocumentSetVersion)),
            "driveItem": lambda n : setattr(self, 'drive_item', n.get_object_value(DriveItem)),
            "fields": lambda n : setattr(self, 'fields', n.get_object_value(FieldValueSet)),
            "sharepointIds": lambda n : setattr(self, 'sharepoint_ids', n.get_object_value(SharepointIds)),
            "versions": lambda n : setattr(self, 'versions', n.get_collection_of_object_values(ListItemVersion)),
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
        writer.write_object_value("analytics", self.analytics)
        writer.write_object_value("contentType", self.content_type)
        writer.write_object_value("deleted", self.deleted)
        writer.write_collection_of_object_values("documentSetVersions", self.document_set_versions)
        writer.write_object_value("driveItem", self.drive_item)
        writer.write_object_value("fields", self.fields)
        writer.write_object_value("sharepointIds", self.sharepoint_ids)
        writer.write_collection_of_object_values("versions", self.versions)
    

