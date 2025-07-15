from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .base_site_page import BaseSitePage
    from .drive import Drive
    from .drive_item import DriveItem
    from .entity import Entity
    from .list_ import List_
    from .list_item import ListItem
    from .recycle_bin import RecycleBin
    from .recycle_bin_item import RecycleBinItem
    from .shared_drive_item import SharedDriveItem
    from .site import Site
    from .site_page import SitePage

from .entity import Entity

@dataclass
class BaseItem(Entity, Parsable):
    
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
        from .list_ import List_
        from .list_item import ListItem
        from .recycle_bin import RecycleBin
        from .recycle_bin_item import RecycleBinItem
        from .shared_drive_item import SharedDriveItem
        from .site import Site
        from .site_page import SitePage

        from .base_site_page import BaseSitePage
        from .drive import Drive
        from .drive_item import DriveItem
        from .entity import Entity
        from .list_ import List_
        from .list_item import ListItem
        from .recycle_bin import RecycleBin
        from .recycle_bin_item import RecycleBinItem
        from .shared_drive_item import SharedDriveItem
        from .site import Site
        from .site_page import SitePage

        fields: dict[str, Callable[[Any], None]] = {
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
    

