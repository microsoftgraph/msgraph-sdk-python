from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

base_item = lazy_import('msgraph.generated.models.base_item')
column_definition = lazy_import('msgraph.generated.models.column_definition')
content_type = lazy_import('msgraph.generated.models.content_type')
drive = lazy_import('msgraph.generated.models.drive')
list_info = lazy_import('msgraph.generated.models.list_info')
list_item = lazy_import('msgraph.generated.models.list_item')
rich_long_running_operation = lazy_import('msgraph.generated.models.rich_long_running_operation')
sharepoint_ids = lazy_import('msgraph.generated.models.sharepoint_ids')
subscription = lazy_import('msgraph.generated.models.subscription')
system_facet = lazy_import('msgraph.generated.models.system_facet')

class List(base_item.BaseItem):
    @property
    def columns(self,) -> Optional[List[column_definition.ColumnDefinition]]:
        """
        Gets the columns property value. The collection of field definitions for this list.
        Returns: Optional[List[column_definition.ColumnDefinition]]
        """
        return self._columns
    
    @columns.setter
    def columns(self,value: Optional[List[column_definition.ColumnDefinition]] = None) -> None:
        """
        Sets the columns property value. The collection of field definitions for this list.
        Args:
            value: Value to set for the columns property.
        """
        self._columns = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new list and sets the default values.
        """
        super().__init__()
        self.odata_type = "#microsoft.graph.list"
        # The collection of field definitions for this list.
        self._columns: Optional[List[column_definition.ColumnDefinition]] = None
        # The collection of content types present in this list.
        self._content_types: Optional[List[content_type.ContentType]] = None
        # The displayable title of the list.
        self._display_name: Optional[str] = None
        # Only present on document libraries. Allows access to the list as a [drive][] resource with [driveItems][driveItem].
        self._drive: Optional[drive.Drive] = None
        # All items contained in the list.
        self._items: Optional[List[list_item.ListItem]] = None
        # Provides additional details about the list.
        self._list: Optional[list_info.ListInfo] = None
        # The collection of long-running operations on the list.
        self._operations: Optional[List[rich_long_running_operation.RichLongRunningOperation]] = None
        # Returns identifiers useful for SharePoint REST compatibility. Read-only.
        self._sharepoint_ids: Optional[sharepoint_ids.SharepointIds] = None
        # The set of subscriptions on the list.
        self._subscriptions: Optional[List[subscription.Subscription]] = None
        # If present, indicates that this is a system-managed list. Read-only.
        self._system: Optional[system_facet.SystemFacet] = None
    
    @property
    def content_types(self,) -> Optional[List[content_type.ContentType]]:
        """
        Gets the contentTypes property value. The collection of content types present in this list.
        Returns: Optional[List[content_type.ContentType]]
        """
        return self._content_types
    
    @content_types.setter
    def content_types(self,value: Optional[List[content_type.ContentType]] = None) -> None:
        """
        Sets the contentTypes property value. The collection of content types present in this list.
        Args:
            value: Value to set for the contentTypes property.
        """
        self._content_types = value
    
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
    
    @property
    def display_name(self,) -> Optional[str]:
        """
        Gets the displayName property value. The displayable title of the list.
        Returns: Optional[str]
        """
        return self._display_name
    
    @display_name.setter
    def display_name(self,value: Optional[str] = None) -> None:
        """
        Sets the displayName property value. The displayable title of the list.
        Args:
            value: Value to set for the displayName property.
        """
        self._display_name = value
    
    @property
    def drive(self,) -> Optional[drive.Drive]:
        """
        Gets the drive property value. Only present on document libraries. Allows access to the list as a [drive][] resource with [driveItems][driveItem].
        Returns: Optional[drive.Drive]
        """
        return self._drive
    
    @drive.setter
    def drive(self,value: Optional[drive.Drive] = None) -> None:
        """
        Sets the drive property value. Only present on document libraries. Allows access to the list as a [drive][] resource with [driveItems][driveItem].
        Args:
            value: Value to set for the drive property.
        """
        self._drive = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "columns": lambda n : setattr(self, 'columns', n.get_collection_of_object_values(column_definition.ColumnDefinition)),
            "content_types": lambda n : setattr(self, 'content_types', n.get_collection_of_object_values(content_type.ContentType)),
            "display_name": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "drive": lambda n : setattr(self, 'drive', n.get_object_value(drive.Drive)),
            "items": lambda n : setattr(self, 'items', n.get_collection_of_object_values(list_item.ListItem)),
            "list": lambda n : setattr(self, 'list', n.get_object_value(list_info.ListInfo)),
            "operations": lambda n : setattr(self, 'operations', n.get_collection_of_object_values(rich_long_running_operation.RichLongRunningOperation)),
            "sharepoint_ids": lambda n : setattr(self, 'sharepoint_ids', n.get_object_value(sharepoint_ids.SharepointIds)),
            "subscriptions": lambda n : setattr(self, 'subscriptions', n.get_collection_of_object_values(subscription.Subscription)),
            "system": lambda n : setattr(self, 'system', n.get_object_value(system_facet.SystemFacet)),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def items(self,) -> Optional[List[list_item.ListItem]]:
        """
        Gets the items property value. All items contained in the list.
        Returns: Optional[List[list_item.ListItem]]
        """
        return self._items
    
    @items.setter
    def items(self,value: Optional[List[list_item.ListItem]] = None) -> None:
        """
        Sets the items property value. All items contained in the list.
        Args:
            value: Value to set for the items property.
        """
        self._items = value
    
    @property
    def list(self,) -> Optional[list_info.ListInfo]:
        """
        Gets the list property value. Provides additional details about the list.
        Returns: Optional[list_info.ListInfo]
        """
        return self._list
    
    @list.setter
    def list(self,value: Optional[list_info.ListInfo] = None) -> None:
        """
        Sets the list property value. Provides additional details about the list.
        Args:
            value: Value to set for the list property.
        """
        self._list = value
    
    @property
    def operations(self,) -> Optional[List[rich_long_running_operation.RichLongRunningOperation]]:
        """
        Gets the operations property value. The collection of long-running operations on the list.
        Returns: Optional[List[rich_long_running_operation.RichLongRunningOperation]]
        """
        return self._operations
    
    @operations.setter
    def operations(self,value: Optional[List[rich_long_running_operation.RichLongRunningOperation]] = None) -> None:
        """
        Sets the operations property value. The collection of long-running operations on the list.
        Args:
            value: Value to set for the operations property.
        """
        self._operations = value
    
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
    
    @property
    def sharepoint_ids(self,) -> Optional[sharepoint_ids.SharepointIds]:
        """
        Gets the sharepointIds property value. Returns identifiers useful for SharePoint REST compatibility. Read-only.
        Returns: Optional[sharepoint_ids.SharepointIds]
        """
        return self._sharepoint_ids
    
    @sharepoint_ids.setter
    def sharepoint_ids(self,value: Optional[sharepoint_ids.SharepointIds] = None) -> None:
        """
        Sets the sharepointIds property value. Returns identifiers useful for SharePoint REST compatibility. Read-only.
        Args:
            value: Value to set for the sharepointIds property.
        """
        self._sharepoint_ids = value
    
    @property
    def subscriptions(self,) -> Optional[List[subscription.Subscription]]:
        """
        Gets the subscriptions property value. The set of subscriptions on the list.
        Returns: Optional[List[subscription.Subscription]]
        """
        return self._subscriptions
    
    @subscriptions.setter
    def subscriptions(self,value: Optional[List[subscription.Subscription]] = None) -> None:
        """
        Sets the subscriptions property value. The set of subscriptions on the list.
        Args:
            value: Value to set for the subscriptions property.
        """
        self._subscriptions = value
    
    @property
    def system(self,) -> Optional[system_facet.SystemFacet]:
        """
        Gets the system property value. If present, indicates that this is a system-managed list. Read-only.
        Returns: Optional[system_facet.SystemFacet]
        """
        return self._system
    
    @system.setter
    def system(self,value: Optional[system_facet.SystemFacet] = None) -> None:
        """
        Sets the system property value. If present, indicates that this is a system-managed list. Read-only.
        Args:
            value: Value to set for the system property.
        """
        self._system = value
    

