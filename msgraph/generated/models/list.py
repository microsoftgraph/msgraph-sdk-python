from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import base_item, column_definition, content_type, drive, list_info, list_item, rich_long_running_operation, sharepoint_ids, subscription, system_facet

from . import base_item

@dataclass
class List(base_item.BaseItem):
    odata_type = "#microsoft.graph.list"
    # The collection of field definitions for this list.
    columns: Optional[List[column_definition.ColumnDefinition]] = None
    # The collection of content types present in this list.
    content_types: Optional[List[content_type.ContentType]] = None
    # The displayable title of the list.
    display_name: Optional[str] = None
    # Only present on document libraries. Allows access to the list as a [drive][] resource with [driveItems][driveItem].
    drive: Optional[drive.Drive] = None
    # All items contained in the list.
    items: Optional[List[list_item.ListItem]] = None
    # Provides additional details about the list.
    list: Optional[list_info.ListInfo] = None
    # The collection of long-running operations on the list.
    operations: Optional[List[rich_long_running_operation.RichLongRunningOperation]] = None
    # Returns identifiers useful for SharePoint REST compatibility. Read-only.
    sharepoint_ids: Optional[sharepoint_ids.SharepointIds] = None
    # The set of subscriptions on the list.
    subscriptions: Optional[List[subscription.Subscription]] = None
    # If present, indicates that this is a system-managed list. Read-only.
    system: Optional[system_facet.SystemFacet] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> List:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: List
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return List()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import base_item, column_definition, content_type, drive, list_info, list_item, rich_long_running_operation, sharepoint_ids, subscription, system_facet

        fields: Dict[str, Callable[[Any], None]] = {
            "columns": lambda n : setattr(self, 'columns', n.get_collection_of_object_values(column_definition.ColumnDefinition)),
            "contentTypes": lambda n : setattr(self, 'content_types', n.get_collection_of_object_values(content_type.ContentType)),
            "displayName": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "drive": lambda n : setattr(self, 'drive', n.get_object_value(drive.Drive)),
            "items": lambda n : setattr(self, 'items', n.get_collection_of_object_values(list_item.ListItem)),
            "list": lambda n : setattr(self, 'list', n.get_object_value(list_info.ListInfo)),
            "operations": lambda n : setattr(self, 'operations', n.get_collection_of_object_values(rich_long_running_operation.RichLongRunningOperation)),
            "sharepointIds": lambda n : setattr(self, 'sharepoint_ids', n.get_object_value(sharepoint_ids.SharepointIds)),
            "subscriptions": lambda n : setattr(self, 'subscriptions', n.get_collection_of_object_values(subscription.Subscription)),
            "system": lambda n : setattr(self, 'system', n.get_object_value(system_facet.SystemFacet)),
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
        writer.write_collection_of_object_values("columns", self.columns)
        writer.write_collection_of_object_values("contentTypes", self.content_types)
        writer.write_str_value("displayName", self.display_name)
        writer.write_object_value("drive", self.drive)
        writer.write_collection_of_object_values("items", self.items)
        writer.write_object_value("list", self.list)
        writer.write_collection_of_object_values("operations", self.operations)
        writer.write_object_value("sharepointIds", self.sharepoint_ids)
        writer.write_collection_of_object_values("subscriptions", self.subscriptions)
        writer.write_object_value("system", self.system)
    

