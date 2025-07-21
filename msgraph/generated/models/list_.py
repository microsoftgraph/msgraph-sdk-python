from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .base_item import BaseItem
    from .column_definition import ColumnDefinition
    from .content_type import ContentType
    from .drive import Drive
    from .list_info import ListInfo
    from .list_item import ListItem
    from .rich_long_running_operation import RichLongRunningOperation
    from .sharepoint_ids import SharepointIds
    from .subscription import Subscription
    from .system_facet import SystemFacet

from .base_item import BaseItem

@dataclass
class List_(BaseItem, Parsable):
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.list"
    # The collection of field definitions for this list.
    columns: Optional[list[ColumnDefinition]] = None
    # The collection of content types present in this list.
    content_types: Optional[list[ContentType]] = None
    # The displayable title of the list.
    display_name: Optional[str] = None
    # Allows access to the list as a drive resource with driveItems. Only present on document libraries.
    drive: Optional[Drive] = None
    # All items contained in the list.
    items: Optional[list[ListItem]] = None
    # Contains more details about the list.
    list_: Optional[ListInfo] = None
    # The collection of long-running operations on the list.
    operations: Optional[list[RichLongRunningOperation]] = None
    # Returns identifiers useful for SharePoint REST compatibility. Read-only.
    sharepoint_ids: Optional[SharepointIds] = None
    # The set of subscriptions on the list.
    subscriptions: Optional[list[Subscription]] = None
    # If present, indicates that the list is system-managed. Read-only.
    system: Optional[SystemFacet] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> List_:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: List_
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return List_()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .base_item import BaseItem
        from .column_definition import ColumnDefinition
        from .content_type import ContentType
        from .drive import Drive
        from .list_info import ListInfo
        from .list_item import ListItem
        from .rich_long_running_operation import RichLongRunningOperation
        from .sharepoint_ids import SharepointIds
        from .subscription import Subscription
        from .system_facet import SystemFacet

        from .base_item import BaseItem
        from .column_definition import ColumnDefinition
        from .content_type import ContentType
        from .drive import Drive
        from .list_info import ListInfo
        from .list_item import ListItem
        from .rich_long_running_operation import RichLongRunningOperation
        from .sharepoint_ids import SharepointIds
        from .subscription import Subscription
        from .system_facet import SystemFacet

        fields: dict[str, Callable[[Any], None]] = {
            "columns": lambda n : setattr(self, 'columns', n.get_collection_of_object_values(ColumnDefinition)),
            "contentTypes": lambda n : setattr(self, 'content_types', n.get_collection_of_object_values(ContentType)),
            "displayName": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "drive": lambda n : setattr(self, 'drive', n.get_object_value(Drive)),
            "items": lambda n : setattr(self, 'items', n.get_collection_of_object_values(ListItem)),
            "list": lambda n : setattr(self, 'list_', n.get_object_value(ListInfo)),
            "operations": lambda n : setattr(self, 'operations', n.get_collection_of_object_values(RichLongRunningOperation)),
            "sharepointIds": lambda n : setattr(self, 'sharepoint_ids', n.get_object_value(SharepointIds)),
            "subscriptions": lambda n : setattr(self, 'subscriptions', n.get_collection_of_object_values(Subscription)),
            "system": lambda n : setattr(self, 'system', n.get_object_value(SystemFacet)),
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
        writer.write_collection_of_object_values("columns", self.columns)
        writer.write_collection_of_object_values("contentTypes", self.content_types)
        writer.write_str_value("displayName", self.display_name)
        writer.write_object_value("drive", self.drive)
        writer.write_collection_of_object_values("items", self.items)
        writer.write_object_value("list", self.list_)
        writer.write_collection_of_object_values("operations", self.operations)
        writer.write_object_value("sharepointIds", self.sharepoint_ids)
        writer.write_collection_of_object_values("subscriptions", self.subscriptions)
        writer.write_object_value("system", self.system)
    

