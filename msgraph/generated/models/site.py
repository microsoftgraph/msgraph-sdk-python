from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import base_item, column_definition, content_type, drive, item_analytics, list, onenote, permission, public_error, rich_long_running_operation, root, sharepoint_ids, site_collection
    from .term_store import store

from . import base_item

@dataclass
class Site(base_item.BaseItem):
    odata_type = "#microsoft.graph.site"
    # Analytics about the view activities that took place in this site.
    analytics: Optional[item_analytics.ItemAnalytics] = None
    # The collection of column definitions reusable across lists under this site.
    columns: Optional[List[column_definition.ColumnDefinition]] = None
    # The collection of content types defined for this site.
    content_types: Optional[List[content_type.ContentType]] = None
    # The full title for the site. Read-only.
    display_name: Optional[str] = None
    # The default drive (document library) for this site.
    drive: Optional[drive.Drive] = None
    # The collection of drives (document libraries) under this site.
    drives: Optional[List[drive.Drive]] = None
    # The error property
    error: Optional[public_error.PublicError] = None
    # The externalColumns property
    external_columns: Optional[List[column_definition.ColumnDefinition]] = None
    # Used to address any item contained in this site. This collection can't be enumerated.
    items: Optional[List[base_item.BaseItem]] = None
    # The collection of lists under this site.
    lists: Optional[List[list.List]] = None
    # Calls the OneNote service for notebook related operations.
    onenote: Optional[onenote.Onenote] = None
    # The collection of long-running operations on the site.
    operations: Optional[List[rich_long_running_operation.RichLongRunningOperation]] = None
    # The permissions associated with the site. Nullable.
    permissions: Optional[List[permission.Permission]] = None
    # If present, indicates that this is the root site in the site collection. Read-only.
    root: Optional[root.Root] = None
    # Returns identifiers useful for SharePoint REST compatibility. Read-only.
    sharepoint_ids: Optional[sharepoint_ids.SharepointIds] = None
    # Provides details about the site's site collection. Available only on the root site. Read-only.
    site_collection: Optional[site_collection.SiteCollection] = None
    # The collection of the sub-sites under this site.
    sites: Optional[List[Site]] = None
    # The default termStore under this site.
    term_store: Optional[store.Store] = None
    # The collection of termStores under this site.
    term_stores: Optional[List[store.Store]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> Site:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: Site
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return Site()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import base_item, column_definition, content_type, drive, item_analytics, list, onenote, permission, public_error, rich_long_running_operation, root, sharepoint_ids, site_collection
        from .term_store import store

        from . import base_item, column_definition, content_type, drive, item_analytics, list, onenote, permission, public_error, rich_long_running_operation, root, sharepoint_ids, site_collection
        from .term_store import store

        fields: Dict[str, Callable[[Any], None]] = {
            "analytics": lambda n : setattr(self, 'analytics', n.get_object_value(item_analytics.ItemAnalytics)),
            "columns": lambda n : setattr(self, 'columns', n.get_collection_of_object_values(column_definition.ColumnDefinition)),
            "contentTypes": lambda n : setattr(self, 'content_types', n.get_collection_of_object_values(content_type.ContentType)),
            "displayName": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "drive": lambda n : setattr(self, 'drive', n.get_object_value(drive.Drive)),
            "drives": lambda n : setattr(self, 'drives', n.get_collection_of_object_values(drive.Drive)),
            "error": lambda n : setattr(self, 'error', n.get_object_value(public_error.PublicError)),
            "externalColumns": lambda n : setattr(self, 'external_columns', n.get_collection_of_object_values(column_definition.ColumnDefinition)),
            "items": lambda n : setattr(self, 'items', n.get_collection_of_object_values(base_item.BaseItem)),
            "lists": lambda n : setattr(self, 'lists', n.get_collection_of_object_values(list.List)),
            "onenote": lambda n : setattr(self, 'onenote', n.get_object_value(onenote.Onenote)),
            "operations": lambda n : setattr(self, 'operations', n.get_collection_of_object_values(rich_long_running_operation.RichLongRunningOperation)),
            "permissions": lambda n : setattr(self, 'permissions', n.get_collection_of_object_values(permission.Permission)),
            "root": lambda n : setattr(self, 'root', n.get_object_value(root.Root)),
            "sharepointIds": lambda n : setattr(self, 'sharepoint_ids', n.get_object_value(sharepoint_ids.SharepointIds)),
            "siteCollection": lambda n : setattr(self, 'site_collection', n.get_object_value(site_collection.SiteCollection)),
            "sites": lambda n : setattr(self, 'sites', n.get_collection_of_object_values(Site)),
            "termStore": lambda n : setattr(self, 'term_store', n.get_object_value(store.Store)),
            "termStores": lambda n : setattr(self, 'term_stores', n.get_collection_of_object_values(store.Store)),
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
    

