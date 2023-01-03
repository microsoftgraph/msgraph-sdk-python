from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

base_item = lazy_import('msgraph.generated.models.base_item')
column_definition = lazy_import('msgraph.generated.models.column_definition')
content_type = lazy_import('msgraph.generated.models.content_type')
drive = lazy_import('msgraph.generated.models.drive')
item_analytics = lazy_import('msgraph.generated.models.item_analytics')
list = lazy_import('msgraph.generated.models.list')
onenote = lazy_import('msgraph.generated.models.onenote')
permission = lazy_import('msgraph.generated.models.permission')
public_error = lazy_import('msgraph.generated.models.public_error')
rich_long_running_operation = lazy_import('msgraph.generated.models.rich_long_running_operation')
root = lazy_import('msgraph.generated.models.root')
sharepoint_ids = lazy_import('msgraph.generated.models.sharepoint_ids')
site_collection = lazy_import('msgraph.generated.models.site_collection')
store = lazy_import('msgraph.generated.models.term_store.store')

class Site(base_item.BaseItem):
    """
    Provides operations to manage the admin singleton.
    """
    @property
    def analytics(self,) -> Optional[item_analytics.ItemAnalytics]:
        """
        Gets the analytics property value. Analytics about the view activities that took place in this site.
        Returns: Optional[item_analytics.ItemAnalytics]
        """
        return self._analytics
    
    @analytics.setter
    def analytics(self,value: Optional[item_analytics.ItemAnalytics] = None) -> None:
        """
        Sets the analytics property value. Analytics about the view activities that took place in this site.
        Args:
            value: Value to set for the analytics property.
        """
        self._analytics = value
    
    @property
    def columns(self,) -> Optional[List[column_definition.ColumnDefinition]]:
        """
        Gets the columns property value. The collection of column definitions reusable across lists under this site.
        Returns: Optional[List[column_definition.ColumnDefinition]]
        """
        return self._columns
    
    @columns.setter
    def columns(self,value: Optional[List[column_definition.ColumnDefinition]] = None) -> None:
        """
        Sets the columns property value. The collection of column definitions reusable across lists under this site.
        Args:
            value: Value to set for the columns property.
        """
        self._columns = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new site and sets the default values.
        """
        super().__init__()
        self.odata_type = "#microsoft.graph.site"
        # Analytics about the view activities that took place in this site.
        self._analytics: Optional[item_analytics.ItemAnalytics] = None
        # The collection of column definitions reusable across lists under this site.
        self._columns: Optional[List[column_definition.ColumnDefinition]] = None
        # The collection of content types defined for this site.
        self._content_types: Optional[List[content_type.ContentType]] = None
        # The full title for the site. Read-only.
        self._display_name: Optional[str] = None
        # The default drive (document library) for this site.
        self._drive: Optional[drive.Drive] = None
        # The collection of drives (document libraries) under this site.
        self._drives: Optional[List[drive.Drive]] = None
        # The error property
        self._error: Optional[public_error.PublicError] = None
        # The externalColumns property
        self._external_columns: Optional[List[column_definition.ColumnDefinition]] = None
        # Used to address any item contained in this site. This collection can't be enumerated.
        self._items: Optional[List[base_item.BaseItem]] = None
        # The collection of lists under this site.
        self._lists: Optional[List[list.List]] = None
        # Calls the OneNote service for notebook related operations.
        self._onenote: Optional[onenote.Onenote] = None
        # The collection of long-running operations on the site.
        self._operations: Optional[List[rich_long_running_operation.RichLongRunningOperation]] = None
        # The permissions associated with the site. Nullable.
        self._permissions: Optional[List[permission.Permission]] = None
        # If present, indicates that this is the root site in the site collection. Read-only.
        self._root: Optional[root.Root] = None
        # Returns identifiers useful for SharePoint REST compatibility. Read-only.
        self._sharepoint_ids: Optional[sharepoint_ids.SharepointIds] = None
        # Provides details about the site's site collection. Available only on the root site. Read-only.
        self._site_collection: Optional[site_collection.SiteCollection] = None
        # The collection of the sub-sites under this site.
        self._sites: Optional[List[Site]] = None
        # The default termStore under this site.
        self._term_store: Optional[store.Store] = None
        # The collection of termStores under this site.
        self._term_stores: Optional[List[store.Store]] = None
    
    @property
    def content_types(self,) -> Optional[List[content_type.ContentType]]:
        """
        Gets the contentTypes property value. The collection of content types defined for this site.
        Returns: Optional[List[content_type.ContentType]]
        """
        return self._content_types
    
    @content_types.setter
    def content_types(self,value: Optional[List[content_type.ContentType]] = None) -> None:
        """
        Sets the contentTypes property value. The collection of content types defined for this site.
        Args:
            value: Value to set for the contentTypes property.
        """
        self._content_types = value
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> Site:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: Site
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return Site()
    
    @property
    def display_name(self,) -> Optional[str]:
        """
        Gets the displayName property value. The full title for the site. Read-only.
        Returns: Optional[str]
        """
        return self._display_name
    
    @display_name.setter
    def display_name(self,value: Optional[str] = None) -> None:
        """
        Sets the displayName property value. The full title for the site. Read-only.
        Args:
            value: Value to set for the displayName property.
        """
        self._display_name = value
    
    @property
    def drive(self,) -> Optional[drive.Drive]:
        """
        Gets the drive property value. The default drive (document library) for this site.
        Returns: Optional[drive.Drive]
        """
        return self._drive
    
    @drive.setter
    def drive(self,value: Optional[drive.Drive] = None) -> None:
        """
        Sets the drive property value. The default drive (document library) for this site.
        Args:
            value: Value to set for the drive property.
        """
        self._drive = value
    
    @property
    def drives(self,) -> Optional[List[drive.Drive]]:
        """
        Gets the drives property value. The collection of drives (document libraries) under this site.
        Returns: Optional[List[drive.Drive]]
        """
        return self._drives
    
    @drives.setter
    def drives(self,value: Optional[List[drive.Drive]] = None) -> None:
        """
        Sets the drives property value. The collection of drives (document libraries) under this site.
        Args:
            value: Value to set for the drives property.
        """
        self._drives = value
    
    @property
    def error(self,) -> Optional[public_error.PublicError]:
        """
        Gets the error property value. The error property
        Returns: Optional[public_error.PublicError]
        """
        return self._error
    
    @error.setter
    def error(self,value: Optional[public_error.PublicError] = None) -> None:
        """
        Sets the error property value. The error property
        Args:
            value: Value to set for the error property.
        """
        self._error = value
    
    @property
    def external_columns(self,) -> Optional[List[column_definition.ColumnDefinition]]:
        """
        Gets the externalColumns property value. The externalColumns property
        Returns: Optional[List[column_definition.ColumnDefinition]]
        """
        return self._external_columns
    
    @external_columns.setter
    def external_columns(self,value: Optional[List[column_definition.ColumnDefinition]] = None) -> None:
        """
        Sets the externalColumns property value. The externalColumns property
        Args:
            value: Value to set for the externalColumns property.
        """
        self._external_columns = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "analytics": lambda n : setattr(self, 'analytics', n.get_object_value(item_analytics.ItemAnalytics)),
            "columns": lambda n : setattr(self, 'columns', n.get_collection_of_object_values(column_definition.ColumnDefinition)),
            "content_types": lambda n : setattr(self, 'content_types', n.get_collection_of_object_values(content_type.ContentType)),
            "display_name": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "drive": lambda n : setattr(self, 'drive', n.get_object_value(drive.Drive)),
            "drives": lambda n : setattr(self, 'drives', n.get_collection_of_object_values(drive.Drive)),
            "error": lambda n : setattr(self, 'error', n.get_object_value(public_error.PublicError)),
            "external_columns": lambda n : setattr(self, 'external_columns', n.get_collection_of_object_values(column_definition.ColumnDefinition)),
            "items": lambda n : setattr(self, 'items', n.get_collection_of_object_values(base_item.BaseItem)),
            "lists": lambda n : setattr(self, 'lists', n.get_collection_of_object_values(list.List)),
            "onenote": lambda n : setattr(self, 'onenote', n.get_object_value(onenote.Onenote)),
            "operations": lambda n : setattr(self, 'operations', n.get_collection_of_object_values(rich_long_running_operation.RichLongRunningOperation)),
            "permissions": lambda n : setattr(self, 'permissions', n.get_collection_of_object_values(permission.Permission)),
            "root": lambda n : setattr(self, 'root', n.get_object_value(root.Root)),
            "sharepoint_ids": lambda n : setattr(self, 'sharepoint_ids', n.get_object_value(sharepoint_ids.SharepointIds)),
            "site_collection": lambda n : setattr(self, 'site_collection', n.get_object_value(site_collection.SiteCollection)),
            "sites": lambda n : setattr(self, 'sites', n.get_collection_of_object_values(Site)),
            "term_store": lambda n : setattr(self, 'term_store', n.get_object_value(store.Store)),
            "term_stores": lambda n : setattr(self, 'term_stores', n.get_collection_of_object_values(store.Store)),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def items(self,) -> Optional[List[base_item.BaseItem]]:
        """
        Gets the items property value. Used to address any item contained in this site. This collection can't be enumerated.
        Returns: Optional[List[base_item.BaseItem]]
        """
        return self._items
    
    @items.setter
    def items(self,value: Optional[List[base_item.BaseItem]] = None) -> None:
        """
        Sets the items property value. Used to address any item contained in this site. This collection can't be enumerated.
        Args:
            value: Value to set for the items property.
        """
        self._items = value
    
    @property
    def lists(self,) -> Optional[List[list.List]]:
        """
        Gets the lists property value. The collection of lists under this site.
        Returns: Optional[List[list.List]]
        """
        return self._lists
    
    @lists.setter
    def lists(self,value: Optional[List[list.List]] = None) -> None:
        """
        Sets the lists property value. The collection of lists under this site.
        Args:
            value: Value to set for the lists property.
        """
        self._lists = value
    
    @property
    def onenote(self,) -> Optional[onenote.Onenote]:
        """
        Gets the onenote property value. Calls the OneNote service for notebook related operations.
        Returns: Optional[onenote.Onenote]
        """
        return self._onenote
    
    @onenote.setter
    def onenote(self,value: Optional[onenote.Onenote] = None) -> None:
        """
        Sets the onenote property value. Calls the OneNote service for notebook related operations.
        Args:
            value: Value to set for the onenote property.
        """
        self._onenote = value
    
    @property
    def operations(self,) -> Optional[List[rich_long_running_operation.RichLongRunningOperation]]:
        """
        Gets the operations property value. The collection of long-running operations on the site.
        Returns: Optional[List[rich_long_running_operation.RichLongRunningOperation]]
        """
        return self._operations
    
    @operations.setter
    def operations(self,value: Optional[List[rich_long_running_operation.RichLongRunningOperation]] = None) -> None:
        """
        Sets the operations property value. The collection of long-running operations on the site.
        Args:
            value: Value to set for the operations property.
        """
        self._operations = value
    
    @property
    def permissions(self,) -> Optional[List[permission.Permission]]:
        """
        Gets the permissions property value. The permissions associated with the site. Nullable.
        Returns: Optional[List[permission.Permission]]
        """
        return self._permissions
    
    @permissions.setter
    def permissions(self,value: Optional[List[permission.Permission]] = None) -> None:
        """
        Sets the permissions property value. The permissions associated with the site. Nullable.
        Args:
            value: Value to set for the permissions property.
        """
        self._permissions = value
    
    @property
    def root(self,) -> Optional[root.Root]:
        """
        Gets the root property value. If present, indicates that this is the root site in the site collection. Read-only.
        Returns: Optional[root.Root]
        """
        return self._root
    
    @root.setter
    def root(self,value: Optional[root.Root] = None) -> None:
        """
        Sets the root property value. If present, indicates that this is the root site in the site collection. Read-only.
        Args:
            value: Value to set for the root property.
        """
        self._root = value
    
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
        writer.write_collection_of_object_values("columns", self.columns)
        writer.write_collection_of_object_values("contentTypes", self.content_types)
        writer.write_str_value("displayName", self.display_name)
        writer.write_object_value("drive", self.drive)
        writer.write_collection_of_object_values("drives", self.drives)
        writer.write_object_value("error", self.error)
        writer.write_collection_of_object_values("externalColumns", self.external_columns)
        writer.write_collection_of_object_values("items", self.items)
        writer.write_collection_of_object_values("lists", self.lists)
        writer.write_object_value("onenote", self.onenote)
        writer.write_collection_of_object_values("operations", self.operations)
        writer.write_collection_of_object_values("permissions", self.permissions)
        writer.write_object_value("root", self.root)
        writer.write_object_value("sharepointIds", self.sharepoint_ids)
        writer.write_object_value("siteCollection", self.site_collection)
        writer.write_collection_of_object_values("sites", self.sites)
        writer.write_object_value("termStore", self.term_store)
        writer.write_collection_of_object_values("termStores", self.term_stores)
    
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
    def site_collection(self,) -> Optional[site_collection.SiteCollection]:
        """
        Gets the siteCollection property value. Provides details about the site's site collection. Available only on the root site. Read-only.
        Returns: Optional[site_collection.SiteCollection]
        """
        return self._site_collection
    
    @site_collection.setter
    def site_collection(self,value: Optional[site_collection.SiteCollection] = None) -> None:
        """
        Sets the siteCollection property value. Provides details about the site's site collection. Available only on the root site. Read-only.
        Args:
            value: Value to set for the siteCollection property.
        """
        self._site_collection = value
    
    @property
    def sites(self,) -> Optional[List[Site]]:
        """
        Gets the sites property value. The collection of the sub-sites under this site.
        Returns: Optional[List[Site]]
        """
        return self._sites
    
    @sites.setter
    def sites(self,value: Optional[List[Site]] = None) -> None:
        """
        Sets the sites property value. The collection of the sub-sites under this site.
        Args:
            value: Value to set for the sites property.
        """
        self._sites = value
    
    @property
    def term_store(self,) -> Optional[store.Store]:
        """
        Gets the termStore property value. The default termStore under this site.
        Returns: Optional[store.Store]
        """
        return self._term_store
    
    @term_store.setter
    def term_store(self,value: Optional[store.Store] = None) -> None:
        """
        Sets the termStore property value. The default termStore under this site.
        Args:
            value: Value to set for the termStore property.
        """
        self._term_store = value
    
    @property
    def term_stores(self,) -> Optional[List[store.Store]]:
        """
        Gets the termStores property value. The collection of termStores under this site.
        Returns: Optional[List[store.Store]]
        """
        return self._term_stores
    
    @term_stores.setter
    def term_stores(self,value: Optional[List[store.Store]] = None) -> None:
        """
        Sets the termStores property value. The collection of termStores under this site.
        Args:
            value: Value to set for the termStores property.
        """
        self._term_stores = value
    

