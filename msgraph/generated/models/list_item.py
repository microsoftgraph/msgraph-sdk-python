from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import base_item, content_type_info, document_set_version, drive_item, field_value_set, item_analytics, list_item_version, sharepoint_ids

from . import base_item

@dataclass
class ListItem(base_item.BaseItem):
    odata_type = "#microsoft.graph.listItem"
    # Analytics about the view activities that took place on this item.
    analytics: Optional[item_analytics.ItemAnalytics] = None
    # The content type of this list item
    content_type: Optional[content_type_info.ContentTypeInfo] = None
    # Version information for a document set version created by a user.
    document_set_versions: Optional[List[document_set_version.DocumentSetVersion]] = None
    # For document libraries, the driveItem relationship exposes the listItem as a [driveItem][]
    drive_item: Optional[drive_item.DriveItem] = None
    # The values of the columns set on this list item.
    fields: Optional[field_value_set.FieldValueSet] = None
    # Returns identifiers useful for SharePoint REST compatibility. Read-only.
    sharepoint_ids: Optional[sharepoint_ids.SharepointIds] = None
    # The list of previous versions of the list item.
    versions: Optional[List[list_item_version.ListItemVersion]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> ListItem:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: ListItem
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return ListItem()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import base_item, content_type_info, document_set_version, drive_item, field_value_set, item_analytics, list_item_version, sharepoint_ids

        fields: Dict[str, Callable[[Any], None]] = {
            "analytics": lambda n : setattr(self, 'analytics', n.get_object_value(item_analytics.ItemAnalytics)),
            "contentType": lambda n : setattr(self, 'content_type', n.get_object_value(content_type_info.ContentTypeInfo)),
            "documentSetVersions": lambda n : setattr(self, 'document_set_versions', n.get_collection_of_object_values(document_set_version.DocumentSetVersion)),
            "driveItem": lambda n : setattr(self, 'drive_item', n.get_object_value(drive_item.DriveItem)),
            "fields": lambda n : setattr(self, 'fields', n.get_object_value(field_value_set.FieldValueSet)),
            "sharepointIds": lambda n : setattr(self, 'sharepoint_ids', n.get_object_value(sharepoint_ids.SharepointIds)),
            "versions": lambda n : setattr(self, 'versions', n.get_collection_of_object_values(list_item_version.ListItemVersion)),
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
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_object_value("analytics", self.analytics)
        writer.write_object_value("contentType", self.content_type)
        writer.write_collection_of_object_values("documentSetVersions", self.document_set_versions)
        writer.write_object_value("driveItem", self.drive_item)
        writer.write_object_value("fields", self.fields)
        writer.write_object_value("sharepointIds", self.sharepoint_ids)
        writer.write_collection_of_object_values("versions", self.versions)
    

