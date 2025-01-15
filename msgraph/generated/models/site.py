from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .base_item import BaseItem
    from .base_site_page import BaseSitePage
    from .column_definition import ColumnDefinition
    from .content_type import ContentType
    from .drive import Drive
    from .item_analytics import ItemAnalytics
    from .list_ import List_
    from .onenote import Onenote
    from .permission import Permission
    from .public_error import PublicError
    from .rich_long_running_operation import RichLongRunningOperation
    from .root import Root
    from .sharepoint_ids import SharepointIds
    from .site_collection import SiteCollection
    from .term_store.store import Store

from .base_item import BaseItem

@dataclass
class Site(BaseItem, Parsable):
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.site"
    # Analytics about the view activities that took place on this site.
    analytics: Optional[ItemAnalytics] = None
    # The collection of column definitions reusable across lists under this site.
    columns: Optional[list[ColumnDefinition]] = None
    # The collection of content types defined for this site.
    content_types: Optional[list[ContentType]] = None
    # The full title for the site. Read-only.
    display_name: Optional[str] = None
    # The default drive (document library) for this site.
    drive: Optional[Drive] = None
    # The collection of drives (document libraries) under this site.
    drives: Optional[list[Drive]] = None
    # The error property
    error: Optional[PublicError] = None
    # The externalColumns property
    external_columns: Optional[list[ColumnDefinition]] = None
    # Identifies whether the site is personal or not. Read-only.
    is_personal_site: Optional[bool] = None
    # Used to address any item contained in this site. This collection can't be enumerated.
    items: Optional[list[BaseItem]] = None
    # The collection of lists under this site.
    lists: Optional[list[List_]] = None
    # Calls the OneNote service for notebook related operations.
    onenote: Optional[Onenote] = None
    # The collection of long-running operations on the site.
    operations: Optional[list[RichLongRunningOperation]] = None
    # The collection of pages in the baseSitePages list in this site.
    pages: Optional[list[BaseSitePage]] = None
    # The permissions associated with the site. Nullable.
    permissions: Optional[list[Permission]] = None
    # If present, provides the root site in the site collection. Read-only.
    root: Optional[Root] = None
    # Returns identifiers useful for SharePoint REST compatibility. Read-only.
    sharepoint_ids: Optional[SharepointIds] = None
    # Provides details about the site's site collection. Available only on the root site. Read-only.
    site_collection: Optional[SiteCollection] = None
    # The collection of the sub-sites under this site.
    sites: Optional[list[Site]] = None
    # The default termStore under this site.
    term_store: Optional[Store] = None
    # The collection of termStores under this site.
    term_stores: Optional[list[Store]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> Site:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: Site
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return Site()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .base_item import BaseItem
        from .base_site_page import BaseSitePage
        from .column_definition import ColumnDefinition
        from .content_type import ContentType
        from .drive import Drive
        from .item_analytics import ItemAnalytics
        from .list_ import List_
        from .onenote import Onenote
        from .permission import Permission
        from .public_error import PublicError
        from .rich_long_running_operation import RichLongRunningOperation
        from .root import Root
        from .sharepoint_ids import SharepointIds
        from .site_collection import SiteCollection
        from .term_store.store import Store

        from .base_item import BaseItem
        from .base_site_page import BaseSitePage
        from .column_definition import ColumnDefinition
        from .content_type import ContentType
        from .drive import Drive
        from .item_analytics import ItemAnalytics
        from .list_ import List_
        from .onenote import Onenote
        from .permission import Permission
        from .public_error import PublicError
        from .rich_long_running_operation import RichLongRunningOperation
        from .root import Root
        from .sharepoint_ids import SharepointIds
        from .site_collection import SiteCollection
        from .term_store.store import Store

        fields: dict[str, Callable[[Any], None]] = {
            "analytics": lambda n : setattr(self, 'analytics', n.get_object_value(ItemAnalytics)),
            "columns": lambda n : setattr(self, 'columns', n.get_collection_of_object_values(ColumnDefinition)),
            "contentTypes": lambda n : setattr(self, 'content_types', n.get_collection_of_object_values(ContentType)),
            "displayName": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "drive": lambda n : setattr(self, 'drive', n.get_object_value(Drive)),
            "drives": lambda n : setattr(self, 'drives', n.get_collection_of_object_values(Drive)),
            "error": lambda n : setattr(self, 'error', n.get_object_value(PublicError)),
            "externalColumns": lambda n : setattr(self, 'external_columns', n.get_collection_of_object_values(ColumnDefinition)),
            "isPersonalSite": lambda n : setattr(self, 'is_personal_site', n.get_bool_value()),
            "items": lambda n : setattr(self, 'items', n.get_collection_of_object_values(BaseItem)),
            "lists": lambda n : setattr(self, 'lists', n.get_collection_of_object_values(List_)),
            "onenote": lambda n : setattr(self, 'onenote', n.get_object_value(Onenote)),
            "operations": lambda n : setattr(self, 'operations', n.get_collection_of_object_values(RichLongRunningOperation)),
            "pages": lambda n : setattr(self, 'pages', n.get_collection_of_object_values(BaseSitePage)),
            "permissions": lambda n : setattr(self, 'permissions', n.get_collection_of_object_values(Permission)),
            "root": lambda n : setattr(self, 'root', n.get_object_value(Root)),
            "sharepointIds": lambda n : setattr(self, 'sharepoint_ids', n.get_object_value(SharepointIds)),
            "siteCollection": lambda n : setattr(self, 'site_collection', n.get_object_value(SiteCollection)),
            "sites": lambda n : setattr(self, 'sites', n.get_collection_of_object_values(Site)),
            "termStore": lambda n : setattr(self, 'term_store', n.get_object_value(Store)),
            "termStores": lambda n : setattr(self, 'term_stores', n.get_collection_of_object_values(Store)),
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
        writer.write_collection_of_object_values("columns", self.columns)
        writer.write_collection_of_object_values("contentTypes", self.content_types)
        writer.write_str_value("displayName", self.display_name)
        writer.write_object_value("drive", self.drive)
        writer.write_collection_of_object_values("drives", self.drives)
        writer.write_object_value("error", self.error)
        writer.write_collection_of_object_values("externalColumns", self.external_columns)
        writer.write_bool_value("isPersonalSite", self.is_personal_site)
        writer.write_collection_of_object_values("items", self.items)
        writer.write_collection_of_object_values("lists", self.lists)
        writer.write_object_value("onenote", self.onenote)
        writer.write_collection_of_object_values("operations", self.operations)
        writer.write_collection_of_object_values("pages", self.pages)
        writer.write_collection_of_object_values("permissions", self.permissions)
        writer.write_object_value("root", self.root)
        writer.write_object_value("sharepointIds", self.sharepoint_ids)
        writer.write_object_value("siteCollection", self.site_collection)
        writer.write_collection_of_object_values("sites", self.sites)
        writer.write_object_value("termStore", self.term_store)
        writer.write_collection_of_object_values("termStores", self.term_stores)
    

