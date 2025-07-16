from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .base_site_page import BaseSitePage
    from .drive import Drive
    from .drive_item import DriveItem
    from .entity import Entity
    from .identity_set import IdentitySet
    from .item_reference import ItemReference
    from .list_ import List_
    from .list_item import ListItem
    from .recycle_bin import RecycleBin
    from .recycle_bin_item import RecycleBinItem
    from .shared_drive_item import SharedDriveItem
    from .site import Site
    from .site_page import SitePage
    from .user import User

from .entity import Entity

@dataclass
class BaseItem(Entity, Parsable):
    # Identity of the user, device, or application that created the item. Read-only.
    created_by: Optional[IdentitySet] = None
    # Identity of the user who created the item. Read-only.
    created_by_user: Optional[User] = None
    # Date and time of item creation. Read-only.
    created_date_time: Optional[datetime.datetime] = None
    # Provides a user-visible description of the item. Optional.
    description: Optional[str] = None
    # ETag for the item. Read-only.
    e_tag: Optional[str] = None
    # Identity of the user, device, and application that last modified the item. Read-only.
    last_modified_by: Optional[IdentitySet] = None
    # Identity of the user who last modified the item. Read-only.
    last_modified_by_user: Optional[User] = None
    # Date and time the item was last modified. Read-only.
    last_modified_date_time: Optional[datetime.datetime] = None
    # The name of the item. Read-write.
    name: Optional[str] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # Parent information, if the item has a parent. Read-write.
    parent_reference: Optional[ItemReference] = None
    # URL that either displays the resource in the browser (for Office file formats), or is a direct link to the file (for other formats). Read-only.
    web_url: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> BaseItem:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: BaseItem
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        try:
            child_node = parse_node.get_child_node("@odata.type")
            mapping_value = child_node.get_str_value() if child_node else None
        except AttributeError:
            mapping_value = None
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.baseSitePage".casefold():
            from .base_site_page import BaseSitePage

            return BaseSitePage()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.drive".casefold():
            from .drive import Drive

            return Drive()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.driveItem".casefold():
            from .drive_item import DriveItem

            return DriveItem()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.list".casefold():
            from .list_ import List_

            return List_()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.listItem".casefold():
            from .list_item import ListItem

            return ListItem()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.recycleBin".casefold():
            from .recycle_bin import RecycleBin

            return RecycleBin()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.recycleBinItem".casefold():
            from .recycle_bin_item import RecycleBinItem

            return RecycleBinItem()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.sharedDriveItem".casefold():
            from .shared_drive_item import SharedDriveItem

            return SharedDriveItem()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.site".casefold():
            from .site import Site

            return Site()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.sitePage".casefold():
            from .site_page import SitePage

            return SitePage()
        return BaseItem()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .base_site_page import BaseSitePage
        from .drive import Drive
        from .drive_item import DriveItem
        from .entity import Entity
        from .identity_set import IdentitySet
        from .item_reference import ItemReference
        from .list_ import List_
        from .list_item import ListItem
        from .recycle_bin import RecycleBin
        from .recycle_bin_item import RecycleBinItem
        from .shared_drive_item import SharedDriveItem
        from .site import Site
        from .site_page import SitePage
        from .user import User

        from .base_site_page import BaseSitePage
        from .drive import Drive
        from .drive_item import DriveItem
        from .entity import Entity
        from .identity_set import IdentitySet
        from .item_reference import ItemReference
        from .list_ import List_
        from .list_item import ListItem
        from .recycle_bin import RecycleBin
        from .recycle_bin_item import RecycleBinItem
        from .shared_drive_item import SharedDriveItem
        from .site import Site
        from .site_page import SitePage
        from .user import User

        fields: dict[str, Callable[[Any], None]] = {
            "createdBy": lambda n : setattr(self, 'created_by', n.get_object_value(IdentitySet)),
            "createdByUser": lambda n : setattr(self, 'created_by_user', n.get_object_value(User)),
            "createdDateTime": lambda n : setattr(self, 'created_date_time', n.get_datetime_value()),
            "description": lambda n : setattr(self, 'description', n.get_str_value()),
            "eTag": lambda n : setattr(self, 'e_tag', n.get_str_value()),
            "lastModifiedBy": lambda n : setattr(self, 'last_modified_by', n.get_object_value(IdentitySet)),
            "lastModifiedByUser": lambda n : setattr(self, 'last_modified_by_user', n.get_object_value(User)),
            "lastModifiedDateTime": lambda n : setattr(self, 'last_modified_date_time', n.get_datetime_value()),
            "name": lambda n : setattr(self, 'name', n.get_str_value()),
            "parentReference": lambda n : setattr(self, 'parent_reference', n.get_object_value(ItemReference)),
            "webUrl": lambda n : setattr(self, 'web_url', n.get_str_value()),
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
        writer.write_object_value("createdBy", self.created_by)
        writer.write_object_value("createdByUser", self.created_by_user)
        writer.write_datetime_value("createdDateTime", self.created_date_time)
        writer.write_str_value("description", self.description)
        writer.write_str_value("eTag", self.e_tag)
        writer.write_object_value("lastModifiedBy", self.last_modified_by)
        writer.write_object_value("lastModifiedByUser", self.last_modified_by_user)
        writer.write_datetime_value("lastModifiedDateTime", self.last_modified_date_time)
        writer.write_str_value("name", self.name)
        writer.write_object_value("parentReference", self.parent_reference)
        writer.write_str_value("webUrl", self.web_url)
    

